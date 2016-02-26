from os.path import realpath, join, dirname

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    here = realpath(dirname(__file__))
    TESTING = True
    DATABASE_PATH = join(here, 'tests', 'test.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig,
}
