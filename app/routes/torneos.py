from flask import Blueprint, jsonify, request
from app import torneo_global

torneos_bp = Blueprint('torneos', __name__)

@torneos_bp.route('/torneos/agregar', methods=['POST'])
def agregar_personaje_torneo():
    """
    Agrega un personaje al torneo.
    """
    data = request.get_json()
    nombre = data.get('nombre')
    nivel_poder = data.get('nivel_poder')

    if not nombre or nivel_poder is None:
        return jsonify({'error': 'Debe proporcionar nombre y nivel_poder'}), 400

    mensaje = torneo_global.agregar_personaje(nivel_poder, nombre)
    return jsonify({'message': mensaje}), 201


@torneos_bp.route('/torneos/siguiente', methods=['GET'])
def siguiente_enfrentamiento():
    """
    Extrae al siguiente personaje para el enfrentamiento.
    """
    proximo = torneo_global.siguiente_enfrentamiento()
    if not proximo:
        return jsonify({'message': 'No hay más personajes en el torneo.'}), 404
    return jsonify({'siguiente_combate': {'nombre': proximo[1], 'nivel_poder': proximo[0]}})


@torneos_bp.route('/torneos/participantes', methods=['GET'])
def mostrar_participantes_torneo():
    """
    Muestra los participantes del torneo en orden de prioridad.
    """
    participantes = torneo_global.mostrar_participantes()
    if not participantes:
        return jsonify({'message': 'No hay participantes en el torneo.'}), 404
    return jsonify({'participantes': participantes})
