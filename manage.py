from app import app,db
from app.models import Users,Pitches
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell():
    return dict(app=app, db=db, Users=Users, Pitches=Pitches)

if __name__ == '__main__':
    manager.run()