from utils.db import db
from dataclasses import dataclass

@dataclass
class tbUbigeo(db.Model):
    __tablename__ = 'tbUbigeo'
    Ubigeo: float
    Distrito: str
    Provincia: str
    Departamento: str
    Poblacion: float
    Superficie: float
    X: float
    Y: float

    Ubigeo = db.Column(db.Numeric, primary_key=True)
    Distrito = db.Column(db.String(100))
    Provincia = db.Column(db.String(100))
    Departamento = db.Column(db.String(100))
    Poblacion = db.Column(db.Numeric)
    Superficie = db.Column(db.Numeric)
    X = db.Column(db.Numeric)
    Y = db.Column(db.Numeric)
