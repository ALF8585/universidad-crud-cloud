# app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Universidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)

class Carrera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    universidad_id = db.Column(db.Integer, db.ForeignKey('universidad.id'), nullable=False)
    universidad = db.relationship('Universidad', backref=db.backref('carreras', lazy=True))
