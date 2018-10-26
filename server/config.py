import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    MIGRATION_DIR = os.path.join('core', 'migrations')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:\
        {passwd}@{host}:5432/{db}'.format(
            user=os.environ.get('DBUSER'),
            passwd=os.environ.get('DBPASS'),
            host=os.environ.get('DBHOST'),
            db=os.environ.get('DBNAME')
        )


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
