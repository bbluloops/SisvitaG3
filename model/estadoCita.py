from utils.db import db
from dataclasses import dataclass

@dataclass
class tbEstadoCita(db.Model):
    __tablename__ = 'tbEstadoCita'
    idEstadoCita: int 
    idCita: int
    estadoCita: str

    idEstadoCita = db.Column(db.Integer, primary_key=True)
    idCita = db.Column(db.Integer, db.ForeignKey('tbCita.idCita'))
    estadoCita = db.Column(db.String(30))

    def __init__(self, idCita, estadoCita):
        self.idCita = idCita
        self.estadoCita = estadoCita