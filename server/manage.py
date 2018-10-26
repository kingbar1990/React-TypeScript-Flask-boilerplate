from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from core import db
from core.views import app


migrate = Migrate(app, db, directory=app.config['MIGRATION_DIR'])
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
