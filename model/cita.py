from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbCita(db.Model):
    __tablename__ = 'tbCita'
    idCita: int 
    idRecomendacionApoyo: int
    idEstudiante: int
    fechaHoraCita: datetime

    idCita = db.Column(db.Integer, primary_key=True)
    idRecomendacionApoyo = db.Column(db.Integer, db.ForeignKey('tbRecomendacionApoyoTratamiento.idRecomendacionApoyo'))
    idEstudiante = db.Column(db.Integer, db.ForeignKey('tbEstudiante.idEstudiante'))
    fechaHoraCita = db.Column(db.DateTime)

    def __init__(self, idRecomendacionApoyo, idEstudiante, fechaHoraCita):
        self.idRecomendacionApoyo = idRecomendacionApoyo
        self.idEstudiante = idEstudiante
        self.fechaHoraCita = fechaHoraCita