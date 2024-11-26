from config.database import db
from datetime import datetime

class Combate(db.Model):
    __tablename__ = 'combates'

    id = db.Column(db.Integer, primary_key=True)
    personaje1_id = db.Column(db.Integer, db.ForeignKey('personajes.id'), nullable=False)
    personaje2_id = db.Column(db.Integer, db.ForeignKey('personajes.id'), nullable=False)
    ganador_id = db.Column(db.Integer, db.ForeignKey('personajes.id'), nullable=True)  # Puede ser nulo en caso de empate
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    resultado = db.Column(db.String(50), nullable=False)  # 'Empate', 'Ganador: Goku', etc.

    # Relaciones
    personaje1 = db.relationship('Personaje', foreign_keys=[personaje1_id], backref='combates_iniciados')
    personaje2 = db.relationship('Personaje', foreign_keys=[personaje2_id], backref='combates_recibidos')
    ganador = db.relationship('Personaje', foreign_keys=[ganador_id], backref='combates_ganados')
