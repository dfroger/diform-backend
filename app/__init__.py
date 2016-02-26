from flask import Flask
from flask.ext import sqlalchemy
from flask.ext import restless

from config import config

db = sqlalchemy.SQLAlchemy()
manager = restless.APIManager(flask_sqlalchemy_db=db)

def create_app(config_name):

    from .model import User, Questionnaire

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    manager.init_app(app)
    with app.app_context():
        manager.create_api(User, methods=['GET', 'POST', 'DELETE'], app=app)
        manager.create_api(Questionnaire, methods=['GET', 'POST', 'DELETE'],
                           app=app)

    return app
