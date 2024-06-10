from utils.db import db
from dataclasses import dataclass

@dataclass
class tbTest(db.Model):
    __tablename__ = 'tbTest'
    idTest: int
    autorTest: str
    descripcionTest: str
    nombreTest: str
#correspondencia ce los atributos de la clase con los de la bd
    idTest = db.Column(db.Integer, primary_key=True)
    autorTest = db.Column(db.String(50))
    descripcionTest = db.Column(db.String(255))
    nombreTest = db.Column(db.String(50))
#definir el constructor
    def __init__(self,autorTest,descripcionTest,nombreTest):
        self.autorTest=autorTest
        self.descripcionTest=descripcionTest
        self.nombreTest=nombreTest
