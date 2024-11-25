from flask import Blueprint, jsonify, request
from app.services.arbol_habilidades_service import arbol_habilidades

habilidades_bp = Blueprint('habilidades', __name__)

@habilidades_bp.route('/habilidades', methods=['GET'])
def mostrar_arbol_habilidades():
    """
    Muestra el árbol de habilidades en formato jerárquico.
    """
    arbol = arbol_habilidades.mostrar_arbol()
    return jsonify({'arbol_habilidades': arbol})

@habilidades_bp.route('/habilidades/agregar', methods=['POST'])
def agregar_habilidad():
    """
    Agrega una nueva habilidad al árbol.
    """
    data = request.get_json()
    nombre_habilidad = data.get('nombre_habilidad')
    habilidad_padre = data.get('habilidad_padre')

    if not nombre_habilidad or not habilidad_padre:
        return jsonify({'error': 'Debe proporcionar nombre_habilidad y habilidad_padre'}), 400

    resultado = arbol_habilidades.agregar_habilidad(nombre_habilidad, habilidad_padre)
    return jsonify({'message': resultado})

@habilidades_bp.route('/habilidades/buscar', methods=['GET'])
def buscar_habilidad():
    """
    Busca una habilidad en el árbol.
    """
    nombre_habilidad = request.args.get('nombre_habilidad')
    if not nombre_habilidad:
        return jsonify({'error': 'Debe proporcionar el nombre_habilidad como parámetro'}), 400

    nodo = arbol_habilidades.buscar_habilidad(arbol_habilidades.raiz, nombre_habilidad)
    if nodo:
        return jsonify({'habilidad_encontrada': nodo.nombre})
    else:
        return jsonify({'error': f"Habilidad '{nombre_habilidad}' no encontrada"}), 404
