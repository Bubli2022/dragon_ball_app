from config.database import db

class Personaje(db.Model):
    __tablename__ = 'personajes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(50), nullable=False)
    nivel_poder = db.Column(db.Integer, default=0, nullable=False)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))

    planeta = db.relationship('Planeta', backref='personajes')
