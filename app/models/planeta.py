from config.database import db

class Planeta(db.Model):
    __tablename__ = 'planetas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)
    distancia_tierra = db.Column(db.Integer, nullable=True)  # Distancia en unidades (opcional)

    # Relación con personajes
    personajes = db.relationship('Personaje', backref='planeta', lazy=True)

    def __repr__(self):
        return f"<Planeta {self.nombre}>"
