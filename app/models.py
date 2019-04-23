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