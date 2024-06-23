from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbRecomendacionApoyoTratamiento(db.Model):
    __tablename__ = 'tbRecomendacionApoyoTratamiento'
    idRecomendacionApoyo: int 
    idEspecialista: int
    idResultadoTest: int
    descripcionRecomendacionApoyo: str
    fechaInicioRecomendacionApoyo: datetime
    fechaFinRecomendacionApoyo: datetime
    nivelAnsiedadRevision: str

    idRecomendacionApoyo = db.Column(db.Integer, primary_key=True)
    idEspecialista = db.Column(db.Integer, db.ForeignKey('tbEspecialistas.idEspecialista'))
    idResultadoTest = db.Column(db.Integer, db.ForeignKey('tbResultadoTest.idResultadoTest'))
    descripcionRecomendacionApoyo = db.Column(db.String(255))
    fechaInicioRecomendacionApoyo = db.Column(db.DateTime)
    fechaFinRecomendacionApoyo = db.Column(db.DateTime)
    nivelAnsiedadRevision = db.Column(db.String(255))

    def __init__(self, idEspecialista, idResultadoTest, descripcionRecomendacionApoyo, fechaInicioRecomendacionApoyo, fechaFinRecomendacionApoyo, nivelAnsiedadRevision):
        self.idEspecialista = idEspecialista
        self.idResultadoTest = idResultadoTest
        self.descripcionRecomendacionApoyo = descripcionRecomendacionApoyo
        self.fechaInicioRecomendacionApoyo = fechaInicioRecomendacionApoyo
        self.fechaFinRecomendacionApoyo = fechaFinRecomendacionApoyo
        self.nivelAnsiedadRevision = nivelAnsiedadRevision