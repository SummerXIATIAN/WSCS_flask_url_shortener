import string
from datetime import datetime
from random import choices

from sympy import public

from .extensions import db

LENGTH = 3

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64),unique=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    admin = db.Column(db.Boolean)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(256))
    short_url = db.Column(db.String(8), unique=True)
    visits = db.Column(db.Integer, default=0)
    data_created = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, default=None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=LENGTH))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()

        return short_url
