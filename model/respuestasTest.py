from utils.db import db
from dataclasses import dataclass

@dataclass
class tbRespuestasTest(db.Model):
    __tablename__ = 'tbRespuestasTest'
    idRespuestas: int
    idTest: int
    idResultadoTest: int
    respuestas: str
    valorRespuesta: float

    idRespuestas = db.Column(db.Integer, primary_key=True)
    idTest = db.Column(db.Integer, db.ForeignKey('tbTest.idTest'))
    idResultadoTest = db.Column(db.Integer, db.ForeignKey('tbResultadoTest.idResultadoTest'))
    respuestas = db.Column(db.String(20))
    valorRespuesta = db.Column(db.Numeric)

#    def __init__(self, idTest, idRegistroSesiones, idResultadoTest, respuestas, valorRespuesta):
 #       self.idTest = idTest
  #      self.idRegistroSesiones = idRegistroSesiones
   #     self.idResultadoTest = idResultadoTest
    #    self.respuestas = respuestas
     #   self.valorRespuesta = valorRespuesta
