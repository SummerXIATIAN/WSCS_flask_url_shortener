from flask import Blueprint, render_template, request, redirect, url_for

from url_shortener.auth import requires_auth

from .extensions import db
from .models import Link

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.visits = link.visits + 1
    db.session.commit()

    return redirect(link.original_url)

@short.route('/<short_url>/del')
@requires_auth
def url_clear(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    db.session.delete(link)
    db.session.commit()
    return  render_template('200.html')

@short.route('/<short_url>/update',methods=['GET', 'POST'])
@requires_auth
def url_update(short_url):
    if request.method == 'POST':
        update_url = request.form['update_url']
        link = Link.query.filter_by(short_url=short_url).first_or_404()
        link.short_url = str(update_url)
        db.session.commit()
        links_all = Link.query.all()
        return  render_template('stats.html', links=links_all)
    else:
        return render_template('update.html')

@short.route('/')
@requires_auth
def index():
    return render_template('index.html')

@short.route('/add_link', methods=['POST'])
@requires_auth
def add_link():
    original_url = request.form['original_url']
    if "https://" not in original_url:
        original_url = "https://"+original_url
    if original_url == "https://":
        return render_template('index.html')
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template('link_added.html', 
        new_link=link.short_url, original_url=link.original_url)

@short.route('/stats')
@requires_auth
def stats():
    links = Link.query.all()

    return render_template('stats.html', links=links)

@short.route('/clear')
def url_clear_all():
    db.session.query(Link).delete()
    db.session.commit()

    return render_template('200.html')

@short.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
