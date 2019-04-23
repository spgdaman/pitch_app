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
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'