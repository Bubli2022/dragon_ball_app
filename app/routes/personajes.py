from flask import Blueprint, jsonify, request
from app.models.personaje import Personaje
from app.services.personaje_service import GestionCombates, SubidaNivel, GestionHabilidades
from app.services.evolucion_service import calcular_evolucion_poder
from app.services.arbol_service import arbol_personajes
# from app.services.arbol_service import ArbolBinarioDeBusqueda
from config.database import db

# from app import arbol_personajes

personajes_bp = Blueprint('personajes', __name__)

@personajes_bp.route('/arbol/insertar', methods=['POST'])
def insertar_en_arbol():
    """
    Inserta un personaje en el árbol binario de búsqueda.
    """
    data = request.get_json()
    nombre = data.get('nombre')
    nivel_poder = data.get('nivel_poder')

    if not nombre or nivel_poder is None:
        return jsonify({'error': 'Debe proporcionar nombre y nivel de poder'}), 400

    arbol_personajes.insertar(nivel_poder, nombre)
    return jsonify({'message': f'Personaje {nombre} con nivel de poder {nivel_poder} agregado al árbol.'}), 201

@personajes_bp.route('/arbol/mas_fuerte', methods=['GET'])
def obtener_mas_fuerte():
    """
    Obtiene el personaje más fuerte del árbol.
    """
    personaje_mas_fuerte = arbol_personajes.buscar_mas_fuerte()
    if personaje_mas_fuerte:
        return jsonify({'personaje_mas_fuerte': personaje_mas_fuerte}), 200
    else:
        return jsonify({'error': 'El árbol está vacío'}), 404

@personajes_bp.route('/arbol/en_orden', methods=['GET'])
def personajes_en_orden():
    """
    Obtiene la lista de personajes ordenados por nivel de poder.
    """
    personajes = arbol_personajes.en_orden()
    return jsonify({'personajes': personajes}), 200

@personajes_bp.route('/personajes', methods=['GET'])
def get_personajes():
    personajes = Personaje.query.all()
    return jsonify([{'id': p.id, 'nombre': p.nombre, 'nivel_poder': p.nivel_poder, 'habilidades': p.habilidades} for p in personajes])

@personajes_bp.route('/personajes', methods=['POST'])
def add_personaje():
    data = request.get_json()
    personaje = Personaje(nombre=data['nombre'], raza=data['raza'], nivel_poder=data['nivel_poder'], planeta_id=data['planeta_id'])
    db.session.add(personaje)
    db.session.commit()
    return jsonify({'message': 'Personaje creado con éxito'}), 201

@personajes_bp.route('/personajes/<int:personaje_id>/subir_nivel', methods=['PUT'])
def subir_nivel(personaje_id):
    data = request.get_json()
    incremento = data.get('incremento', 0)
    try:
        personaje = SubidaNivel.subir_nivel(personaje_id, incremento)
        return jsonify({'message': f'{personaje.nombre} ha subido de nivel.', 'nivel_poder': personaje.nivel_poder}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@personajes_bp.route('/personajes/<int:personaje_id>/aprender_habilidad', methods=['PUT'])
def aprender_habilidad(personaje_id):
    data = request.get_json()
    habilidad = data.get('habilidad')
    try:
        personaje = GestionHabilidades.aprender_habilidad(personaje_id, habilidad)
        return jsonify({'message': f'{personaje.nombre} ha aprendido la habilidad: {habilidad}'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@personajes_bp.route('/combate', methods=['POST'])
def combate():
    data = request.get_json()
    personaje1 = Personaje.query.get(data['personaje1_id'])
    personaje2 = Personaje.query.get(data['personaje2_id'])

    if personaje1 and personaje2:
        ganador = GestionCombates.combate(personaje1, personaje2)
        return jsonify({'ganador': ganador.nombre if ganador else 'Empate'}), 200
    else:
        return jsonify({'error': 'Personaje(s) no encontrado(s).'}), 404

@personajes_bp.route('/personajes/<int:personaje_id>/evolucionar', methods=['PUT'])
def evolucionar_poder(personaje_id):
    """
    Endpoint para calcular la evolución del nivel de poder de un personaje.
    :param personaje_id: ID del personaje en la base de datos.
    """
    data = request.get_json()
    multiplicadores = data.get('multiplicadores', [])

    if not multiplicadores:
        return jsonify({'error': 'Debe proporcionar una lista de multiplicadores'}), 400

    personaje = Personaje.query.get(personaje_id)
    if not personaje:
        return jsonify({'error': 'Personaje no encontrado'}), 404

    try:
        nivel_final = calcular_evolucion_poder(personaje.nivel_poder, multiplicadores)
        personaje.nivel_poder = int(nivel_final)  # Actualizar el nivel en la base de datos
        db.session.commit()
        return jsonify({
            'message': f'{personaje.nombre} ha evolucionado su nivel de poder.',
            'nivel_poder_inicial': personaje.nivel_poder,
            'nivel_poder_final': nivel_final,
            'multiplicadores': multiplicadores
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    