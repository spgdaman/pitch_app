from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User:
    def __init__(self, firstname,lastname,email,username,password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password

class Credentials:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Pitch:
    def __init__(self, pitch):
        self.pitch = pitch
        self.upvote = upvote
        self.downvote = downvote

    # def upvote(self):
    #     self.upvote += 1

    # def downvote(self):
    #     self.downvote -= 1

class Users(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    username = db.Column(db.String(255), index = True)
    password = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.pass_secure =generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Pitches(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.String(255))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    user = db.relationship('Users',backref='pitches', lazy="dynamic")

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))