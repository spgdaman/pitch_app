from . import db

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

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def __repr__(self):
        return f'User {self.username}'

class Pitches(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.String(255))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    user = db.relationship('Users',backref='pitches', lazy="dynamic")