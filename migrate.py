from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from project.model import db
from project import create_app

app = create_app('config.py')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
