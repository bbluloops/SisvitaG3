from utils.db import db
from dataclasses import dataclass

@dataclass
class tbOpcionesTest(db.Model):
    __tablename__ = 'tbOpcionesTest'
    idOpcionTest: int 
    idPreguntaTest: int
    respuestaOpcionTest: str
    puntajeOpcionTest: float

    idOpcionTest = db.Column(db.Integer, primary_key=True)
    idPreguntaTest = db.Column(db.Integer, db.ForeignKey('tbPreguntasTest.idPreguntaTest'))
    respuestaOpcionTest = db.Column(db.String(255))
    puntajeOpcionTest = db.Column(db.Numeric)

    def __init__(self, idPreguntaTest, respuestaOpcionTest, puntajeOpcionTest):
        self.idPreguntaTest = idPreguntaTest
        self.respuestaOpcionTest = respuestaOpcionTest
        self.puntajeOpcionTest = puntajeOpcionTest