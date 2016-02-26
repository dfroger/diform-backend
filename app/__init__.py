from flask import Flask
from flask.ext import sqlalchemy
from flask.ext import restless

from config import config

db = sqlalchemy.SQLAlchemy()
manager = restless.APIManager()

def create_app(config_name):
    from .model import User, Questionnaire

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    manager.init_app(app, flask_sqlalchemy_db=db)
    manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Questionnaire, methods=['GET', 'POST', 'DELETE'])

    return app
