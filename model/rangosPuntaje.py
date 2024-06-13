from utils.db import db
from dataclasses import dataclass

@dataclass
class tbRangosPuntaje(db.Model):
    __tablename__ = 'tbRangosPuntaje'
    idRangoTest: int
    idTest: int
    minimoPuntaje: float
    maximoPuntaje: float
    interpretacionPuntaje: str

    idRangoTest = db.Column(db.Integer, primary_key=True)
    idTest = db.Column(db.Integer, db.ForeignKey('tbTest.idTest'))
    minimoPuntaje = db.Column(db.Numeric)
    maximoPuntaje = db.Column(db.Numeric)
    interpretacionPuntaje = db.Column(db.String(255))

    def __init__(self, idTest, minimoPuntaje, maximoPuntaje, interpretacionPuntaje):
      self.idTest = idTest
      self.minimoPuntaje = minimoPuntaje
      self.maximoPuntaje = maximoPuntaje
      self.interpretacionPuntaje = interpretacionPuntaje
