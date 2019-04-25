from app import create_app,db
from app.models import Users,Pitches
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('server',Server)
#manager.add_command('migrate',MigrateCommand)

@manager.shell
def make_shell():
    return dict(app=app, db=db, Users=Users, Pitches=Pitches)

if __name__ == '__main__':
    manager.run()