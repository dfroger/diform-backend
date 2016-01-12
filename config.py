from os.path import realpath, join, dirname

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    here = realpath(dirname(__file__))
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(here, 'test.db')