from datetime import date
from app import db
from dataclasses import dataclass
from app.infraestructure.mysql_database import DataBaseConfig
from sqlalchemy import func

@dataclass
class Question(db.Model):
    fecha: date
    titular: str
    hecho: str
    tipo: str
    tags: str

    __tablename__ = 'test__question'

    # Asociar la instancia de MetaData con la tabla
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    titular = db.Column(db.String(250), nullable=True)
    hecho = db.Column(db.String(800), nullable=True)
    tipo = db.Column(db.String(100), nullable=True)
    tags = db.Column(db.String(250), nullable=True)

    def __init__(self, fecha, titular, hecho, tipo, tags):
        self.fecha = fecha
        self.titular = titular
        self.hecho = hecho
        self.tipo = tipo
        self.tags = tags