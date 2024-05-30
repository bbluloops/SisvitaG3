from utils.db import db
from dataclasses import dataclass

@dataclass
class tbEstudiante(db.Model):
    idEstudiante: int
    nombreEstudiante: str
    apellidoEstudiante: str
    correoEstudiante: str
    contraseñaEstudiante: str

    idEstudiante = db.Column(db.Integer, primary_key=True)
    nombreEstudiante=db.Column(db.String(100))
    apellidoEstudiante=db.Column(db.String(100))
    correoEstudiante=db.Column(db.String(100))
    contraseñaEstudiante=db.Column(db.String(100))

    def __init__(self, nombreEstudiante, apellidoEstudiante, correoEstudiante, contraseñaEstudiante):
        self.nombreEstudiante=nombreEstudiante
        self.apellidoEstudiante=apellidoEstudiante
        self.correoEstudiante=correoEstudiante
        self.contraseñaEstudiante=contraseñaEstudiante
        



