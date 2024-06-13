from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class tbHorarioEspecialista(db.Model):
    __tablename__ = 'tbHorarioEspecialista'
    idHorarioEspecialista: int 
    idEspecialista: int
    diaHorarioEspecialista: datetime
    horaInicioHorarioEspecialista: datetime
    horaFinHorarioEspecialista: datetime

    idHorarioEspecialista = db.Column(db.Integer, primary_key=True)
    idEspecialista = db.Column(db.Integer, db.ForeignKey('tbEspecialistas.idEspecialista'))
    diaHorarioEspecialista = db.Column(db.Date)
    horaInicioHorarioEspecialista = db.Column(db.DateTime)
    horaFinHorarioEspecialista = db.Column(db.DateTime)

    def __init__(self, idEspecialista, diaHorarioEspecialista, horaInicioHorarioEspecialista, horaFinHorarioEspecialista):
        self.idEspecialista = idEspecialista
        self.diaHorarioEspecialista = diaHorarioEspecialista
        self.horaInicioHorarioEspecialista = horaInicioHorarioEspecialista
        self.horaFinHorarioEspecialista = horaFinHorarioEspecialista