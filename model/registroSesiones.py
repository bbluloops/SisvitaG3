from utils.db import db
from dataclasses import dataclass

@dataclass
class tbRegistroSesionesHistorial(db.Model):
    __tablename__ = 'tbRegistroSesionesHistorial'
    idRegistroSesiones: int
    idEstudiante: int

    idRegistroSesiones = db.Column(db.Integer, primary_key=True)
    idEstudiante = db.Column(db.Integer, db.ForeignKey('tbEstudiante.idEstudiante'))

    def __init__(self, idEstudiante):
        self.idEstudiante = idEstudiante