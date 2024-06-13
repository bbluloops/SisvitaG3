from utils.db import db
from dataclasses import dataclass

@dataclass
class tbEspecialidad(db.Model):
    __tablename__ = 'tbEspecialidad'
    idEspecialidad: int 
    idEspecialista: int
    nombreEspecialidad: str

    idEspecialidad = db.Column(db.Integer, primary_key=True)
    idEspecialista = db.Column(db.Integer, db.ForeignKey('tbEspecialistas.idEspecialista'))
    nombreEspecialidad = db.Column(db.String(100))

    def __init__(self, idEspecialista, nombreEspecialidad):
        self.idEspecialista = idEspecialista
        self.nombreEspecialidad = nombreEspecialidad