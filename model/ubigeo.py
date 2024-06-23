from utils.db import db
from dataclasses import dataclass

@dataclass
class tbUbigeo(db.Model):
    __tablename__ = 'tbUbigeo'
    idUbigeo: str 
    Distrito: str
    Provincia: str
    Departamento: str
    Poblacion: float
    Superficie: float
    X: float
    Y: float

    idUbigeo = db.Column(db.String(6), primary_key=True)
    Distrito = db.Column(db.String(100))
    Provincia = db.Column(db.String(100))
    Departamento = db.Column(db.String(100))
    Poblacion = db.Column(db.Numeric)
    Superficie = db.Column(db.Numeric)
    X = db.Column(db.Numeric)
    Y = db.Column(db.Numeric)

    def __init__(self, idUbigeo, Distrito, Provincia, Departamento, Poblacion, Superficie, X, Y):
        self.idUbigeo = idUbigeo
        self.Distrito = Distrito
        self.Provincia = Provincia
        self.Departamento = Departamento
        self.Poblacion = Poblacion
        self.Superficie = Superficie
        self.X = X
        self.Y = Y
