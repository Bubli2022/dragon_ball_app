from flask import Blueprint, jsonify, request
from app.services.combate_service import CombateService
from app.models.combate import Combate

combates_bp = Blueprint('combates', __name__)

@combates_bp.route('/combates', methods=['POST'])
def registrar_combate():
    """
    Registra un nuevo combate entre dos personajes.
    """
    data = request.get_json()
    personaje1_id = data.get('personaje1_id')
    personaje2_id = data.get('personaje2_id')

    if not personaje1_id or not personaje2_id:
        return jsonify({'error': 'Debe proporcionar los IDs de los dos personajes.'}), 400

    try:
        combate = CombateService.ejecutar_combate(personaje1_id, personaje2_id)
        return jsonify({
            'id': combate.id,
            'personaje1': combate.personaje1.nombre,
            'personaje2': combate.personaje2.nombre,
            'ganador': combate.ganador.nombre if combate.ganador else 'Empate',
            'fecha': combate.fecha,
            'resultado': combate.resultado
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 404


@combates_bp.route('/combates', methods=['GET'])
def listar_combates():
    """
    Obtiene todos los combates registrados.
    """
    combates = Combate.query.all()
    return jsonify([{
        'id': c.id,
        'personaje1': c.personaje1.nombre,
        'personaje2': c.personaje2.nombre,
        'ganador': c.ganador.nombre if c.ganador else 'Empate',
        'fecha': c.fecha,
        'resultado': c.resultado
    } for c in combates])
