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
