from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbEspecialistas(db.Model):
    idEspecialista: int
    nombreEspecialista: str
    apellidoEspecialista: str
    correoEspecialista: str
    contraseñaEspecialista: str

    idEspecialista = db.Column(db.Integer, primary_key=True)
    nombreEspecialista=db.Column(db.String(100))
    apellidoEspecialista=db.Column(db.String(100))
    correoEspecialista=db.Column(db.String(100))
    contraseñaEspecialista=db.Column(db.String(100))

    def _init_(self, nombreEspecialista, apellidoEspecialista, correoEspecialista, contraseñaEspecialista):
        self.nombreEspecialista=nombreEspecialista
        self.apellidoEspecialista=apellidoEspecialista
        self.correoEspecialista=correoEspecialista
        self.contraseñaEspecialista=contraseñaEspecialista