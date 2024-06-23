from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbEstudiante(db.Model):
    __tablename__ = 'tbEstudiante' 
    idEstudiante: int
    nombreEstudiante: str
    apellidoEstudiante: str
    correoEstudiante: str
    contraseñaEstudiante: str
    Ubigeo: float

    idEstudiante = db.Column(db.Integer, primary_key=True)
    nombreEstudiante=db.Column(db.String(100))
    apellidoEstudiante=db.Column(db.String(100))
    correoEstudiante=db.Column(db.String(100))
    contraseñaEstudiante=db.Column(db.String(100))
    Ubigeo = db.Column(db.Numeric, db.ForeignKey('tbUbigeo.Ubigeo'))

    def __init__(self, nombreEstudiante, apellidoEstudiante, correoEstudiante, contraseñaEstudiante, Ubigeo):
        self.nombreEstudiante=nombreEstudiante
        self.apellidoEstudiante=apellidoEstudiante
        self.correoEstudiante=correoEstudiante
        self.contraseñaEstudiante=contraseñaEstudiante
        self.Ubigeo=Ubigeo
        



