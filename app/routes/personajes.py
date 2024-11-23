from flask import Blueprint, request, jsonify
from app.models.personaje import Personaje
from config.database import db

personajes_bp = Blueprint('personajes', __name__)

@personajes_bp.route('/personajes', methods=['GET'])
def get_personajes():
    personajes = Personaje.query.all()
    return jsonify([{'id': p.id, 'nombre': p.nombre, 'nivel_poder': p.nivel_poder} for p in personajes])

@personajes_bp.route('/personajes', methods=['POST'])
def add_personaje():
    data = request.get_json()
    personaje = Personaje(nombre=data['nombre'], raza=data['raza'], nivel_poder=data['nivel_poder'], planeta_id=data['planeta_id'])
    db.session.add(personaje)
    db.session.commit()
    return jsonify({'message': 'Personaje creado con éxito'}), 201
