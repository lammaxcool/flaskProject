import os
basedir = os.path.abspath(os.path.dirname(__file__))


# export APP_SETTINGS=config.'one of possible config state'
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = 'this-really-needs-to-be-changed'
    # export DATABASE_URL="postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


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
