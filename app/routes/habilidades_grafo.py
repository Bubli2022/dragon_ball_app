from flask import Blueprint, jsonify, request
from app import grafo_habilidades

habilidades_grafo_bp = Blueprint('habilidades_grafo', __name__)

@habilidades_grafo_bp.route('/habilidades', methods=['POST'])
def agregar_habilidad():
    """
    Agrega una habilidad al grafo.
    """
    data = request.get_json()
    habilidad = data.get('habilidad')

    if not habilidad:
        return jsonify({'error': 'Debe proporcionar el nombre de la habilidad.'}), 400

    grafo_habilidades.agregar_habilidad(habilidad)
    return jsonify({'message': f"Habilidad '{habilidad}' agregada al grafo."}), 201


@habilidades_grafo_bp.route('/habilidades/dependencia', methods=['POST'])
def agregar_dependencia():
    """
    Agrega una dependencia entre dos habilidades.
    """
    data = request.get_json()
    habilidad_previa = data.get('habilidad_previa')
    habilidad_siguiente = data.get('habilidad_siguiente')

    if not all([habilidad_previa, habilidad_siguiente]):
        return jsonify({'error': 'Debe proporcionar habilidad_previa y habilidad_siguiente.'}), 400

    grafo_habilidades.agregar_dependencia(habilidad_previa, habilidad_siguiente)
    return jsonify({'message': f"Dependencia agregada: '{habilidad_previa}' -> '{habilidad_siguiente}'."}), 201


@habilidades_grafo_bp.route('/habilidades/orden', methods=['GET'])
def obtener_orden_topologico():
    """
    Obtiene el orden topológico de las habilidades.
    """
    orden = grafo_habilidades.orden_topologico()
    if orden:
        return jsonify({'orden': orden})
    else:
        return jsonify({'error': 'Error: Hay un ciclo en las dependencias de habilidades.'}), 400
