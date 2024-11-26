from config.database import db
from sqlalchemy.dialects.postgresql import JSON

class Habilidad(db.Model):
    __tablename__ = 'habilidades'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)
    personajes = db.Column(JSON, default=list)  # Personajes que tienen esta habilidad
    habilidad_padre_id = db.Column(db.Integer, db.ForeignKey('habilidades.id'), nullable=True)

    # Relación jerárquica: Una habilidad puede tener una habilidad "padre"
    habilidad_padre = db.relationship('Habilidad', remote_side=[id], backref='habilidades_hijas')

    def __repr__(self):
        return f"<Habilidad {self.nombre}>"
