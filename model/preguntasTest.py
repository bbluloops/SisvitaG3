from utils.db import db
from dataclasses import dataclass

@dataclass
class tbPreguntasTest(db.Model):
    __tablename__ = 'tbPreguntasTest'
    idPreguntaTest: int
    idTest: int
    enunciadoPreguntaTest: str

    idPreguntaTest = db.Column(db.Integer, primary_key=True)
    idTest = db.Column(db.Integer, db.ForeignKey('tbTest.idTest'))
    enunciadoPreguntaTest = db.Column(db.String(255))