from flask import Flask
from flask.ext import sqlalchemy
from flask.ext import restless

app = Flask(__name__)

db = sqlalchemy.SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filler = db.relationship('User', backref=db.backref('Questionnaire',
                                                        lazy='dynamic'))
    filler_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    some_number = db.Column(db.Integer)
    some_text = db.Column(db.Unicode)

def init_db():
    db.create_all()

    manager = restless.APIManager(app, flask_sqlalchemy_db=db)
    manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
    manager.create_api(Questionnaire, methods=['GET', 'POST', 'DELETE'])

if __name__ == '__main__':
    app.config.from_object('config.DevelopmentConfig')
    app.run()
