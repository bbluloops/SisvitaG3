from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbResultadoTest(db.Model):
    __tablename__ = 'tbResultadoTest'
    idResultadoTest: int
    puntajeResultadoTest: float
    infoResultado: str
    fechaResultadoTest: datetime
    idRegistroSesiones: int
    revisadoResultadoTest: bool

    idResultadoTest = db.Column(db.Integer, primary_key=True)
    puntajeResultadoTest = db.Column(db.Numeric)
    infoResultado = db.Column(db.String(100))
    fechaResultadoTest = db.Column(db.Date)
    idRegistroSesiones = db.Column(db.Integer, db.ForeignKey(
        'tbRegistroSesionesHistorial.idRegistroSesiones'))
    revisadoResultadoTest = db.Column(db.Boolean)

    def __init__(self, puntajeResultadoTest, infoResultado, fechaResultadoTest, idRegistroSesiones, revisadoResultadoTest):
        self.puntajeResultadoTest = puntajeResultadoTest
        self.infoResultado = infoResultado
        self.fechaResultadoTest = fechaResultadoTest
        self.idRegistroSesiones = idRegistroSesiones
        self.revisadoResultadoTest = revisadoResultadoTest
