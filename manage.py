from app import app,db
from app.models import Users,Pitches
from flask_script import Manager, Server

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell():
    return dict(app=app, db=db, Users=Users, Pitches=Pitches)

if __name__ == '__main__':
    manager.run()