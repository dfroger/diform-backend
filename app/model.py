from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    questionnaires = db.relationship('Questionnaire', back_populates='filler')

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filler_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    filler = db.relationship('User', back_populates="questionnaires")
    some_number = db.Column(db.Integer)
    some_text = db.Column(db.Unicode)
