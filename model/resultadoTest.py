from utils.db import db
from dataclasses import dataclass

@dataclass
class tbResultadoTest(db.Model):
    __tablename__ = 'tbResultadoTest'
    idResultadoTest: int
    puntajeResultadoTest: float
    infoResultado: str
    fechaResultadoTest: str

    idResultadoTest = db.Column(db.Integer, primary_key=True)
    puntajeResultadoTest = db.Column(db.Numeric)
    infoResultado = db.Column(db.String(100))
    fechaResultadoTest = db.Column(db.Date)

    def __init__(self, puntajeResultadoTest, infoResultado, fechaResultadoTest):
        self.puntajeResultadoTest = puntajeResultadoTest
        self.infoResultado = infoResultado
        self.fechaResultadoTest = fechaResultadoTest
