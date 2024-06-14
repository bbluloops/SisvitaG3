from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbRecomendacionApoyoTratamiento(db.Model):
    __tablename__ = 'tbRecomendacionApoyoTratamiento'
    idRecomendacionApoyo: int 
    idEspecialista: int
    idRespuestas: int
    descripcionRecomendacionApoyo: str
    fechaInicioRecomendacionApoyo: datetime
    fechaFinRecomendacionApoyo: datetime

    idRecomendacionApoyo = db.Column(db.Integer, primary_key=True)
    idEspecialista = db.Column(db.Integer, db.ForeignKey('tbEspecialistas.idEspecialista'))
    idRespuestas = db.Column(db.Integer, db.ForeignKey('tbRespuestasTest.idRespuestas'))
    descripcionRecomendacionApoyo = db.Column(db.String(255))
    fechaInicioRecomendacionApoyo = db.Column(db.DateTime)
    fechaFinRecomendacionApoyo = db.Column(db.DateTime)

    def __init__(self, idEspecialista, idRespuestas, descripcionRecomendacionApoyo, fechaInicioRecomendacionApoyo, fechaFinRecomendacionApoyo):
        self.idEspecialista = idEspecialista
        self.idRespuestas = idRespuestas
        self.descripcionRecomendacionApoyo = descripcionRecomendacionApoyo
        self.fechaInicioRecomendacionApoyo = fechaInicioRecomendacionApoyo
        self.fechaFinRecomendacionApoyo = fechaFinRecomendacionApoyo