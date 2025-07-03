from app.models import Universidad, Carrera
from app.routes import app


class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
