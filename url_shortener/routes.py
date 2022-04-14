from flask import Blueprint, render_template, request, redirect, url_for, jsonify, make_response
import re
import uuid
from url_shortener.auth import requires_auth
from random import choices
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime,timedelta
from functools import wraps


from .settings import SECRET_KEY
from .extensions import db
from .models import Link, User

################ 
################ 
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing!'}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = User.query.filter_by(user_id=data['user_id']).first()
        except Exception as e:
            return jsonify({'message':'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)

    return decorated

short = Blueprint('short', __name__)

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

@short.route('/<short_url>')
# @token_required
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.visits = link.visits + 1
    db.session.commit()
    return redirect(link.original_url)

@short.route('/')
# @requires_auth
@token_required
def index(current_user):
    return render_template('index.html')

@short.route('/add_link', methods=['POST'])
# @requires_auth
@token_required
def add_link(current_user):
    original_url = request.form['original_url']
    if "https://" not in original_url:
        original_url = "https://"+original_url
    if original_url == "https://":
        return render_template('index.html')

    if re.match(regex, original_url) is not None:
        link = Link(original_url=original_url)
        db.session.add(link)
        db.session.commit()
        return render_template('link_added.html',
            new_link=link.short_url, original_url=link.original_url)
    else:
        return render_template('index.html')

@short.route('/stats')
# @requires_auth
# @token_required
def stats():
    links = Link.query.all()
    return render_template('stats.html', links=links)

@short.route('/<short_url>/del')
# @requires_auth
@token_required
def url_clear(current_user,short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    db.session.delete(link)
    db.session.commit()
    return  render_template('200.html')

@short.route('/clear')
@token_required
def url_clear_all(current_user):
    db.session.query(Link).delete()
    db.session.commit()
    return render_template('200.html')

@short.route('/<short_url>/update',methods=['GET', 'POST'])
# @requires_auth
@token_required
def url_update(current_user,short_url):
    if request.method == 'POST':
        update_url = request.form['update_url']
        if not update_url:
            update_url = ''.join(choices('0123456789', k=4))
        link = Link.query.filter_by(short_url=short_url).first_or_404()
        link.short_url = str(update_url)
        db.session.commit()
        links_all = Link.query.all()
        return  render_template('stats.html', links=links_all)
    else:
        return render_template('update.html')

@short.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

# user system #
# ###
# ###
@short.route('/user',methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({'message':'You are not allowed'})

    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['user_id'] = user.user_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users':output})

@short.route('/user',methods=['POST'])
# @token_required
def create_user():
    # if not current_user.admin:
        # return jsonify({'message':'You are not allowed'})

    data = request.get_json()
    hashed_pwd = generate_password_hash(data['password'], method='sha256')
    new_user = User(user_id=str(uuid.uuid4()), name=data['name'], password=hashed_pwd, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message':'New user created!'})

@short.route('/user/<user_id>',methods=['GET'])
@token_required
def get_one_user(current_user,user_id):
    if not current_user.admin:
        return jsonify({'message':'You are not allowed'})

    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message':'No user found!'})
    
    user_data = {}
    user_data['user_id'] = user.user_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    return jsonify({'users':user_data})

@short.route('/user/<user_id>',methods=['PUT'])
# @token_required
def promote_user(user_id):
    # if not current_user.admin:
        # return jsonify({'message':'You are not allowed'})

    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message':'No user found!'})
    user.admin = True
    db.session.commit()
    return jsonify({'message':'User has been promoted'})

@short.route('/user/<user_id>',methods=['DELETE'])
@token_required
def delete_user(current_user,user_id):
    if not current_user.admin:
        return jsonify({'message':'You are not allowed'})

    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message':'No user found!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message':'User has been deleted'})

@short.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Please enter Username or Password',401,{'WWW-Authenticate':'Basic realm="Login Required!"'})
    
    user = User.query.filter_by(name=auth.username).first()
    if not user:
        return make_response('User does not exist',401,{'WWW-Authenticate':'Basic realm="Login Required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'user_id': user.user_id,
                            'exp':datetime.utcnow()+timedelta(minutes=120)}
                            ,SECRET_KEY, algorithm='HS256')
        return jsonify({'token':token}),redirect(url_for('short.index',token=token))
    
    return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login Required!"'})