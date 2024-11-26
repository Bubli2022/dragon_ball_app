from flask import Blueprint, jsonify, request
from app.services.planeta_service import PlanetaService

planetas_bp = Blueprint('planetas', __name__)

@planetas_bp.route('/planetas', methods=['GET'])
def listar_planetas():
    """
    Obtiene la lista de planetas.
    """
    planetas = PlanetaService.listar_planetas()
    return jsonify([{
        'id': p.id,
        'nombre': p.nombre,
        'descripcion': p.descripcion,
        'distancia_tierra': p.distancia_tierra
    } for p in planetas])

@planetas_bp.route('/planetas', methods=['POST'])
def agregar_planeta():
    """
    Agrega un nuevo planeta.
    """
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    distancia_tierra = data.get('distancia_tierra')

    if not nombre:
        return jsonify({'error': 'Debe proporcionar el nombre del planeta.'}), 400

    try:
        planeta = PlanetaService.agregar_planeta(nombre, descripcion, distancia_tierra)
        return jsonify({
            'id': planeta.id,
            'nombre': planeta.nombre,
            'descripcion': planeta.descripcion,
            'distancia_tierra': planeta.distancia_tierra
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@planetas_bp.route('/planetas/<string:nombre>', methods=['GET'])
def buscar_planeta(nombre):
    """
    Busca un planeta por su nombre.
    """
    planeta = PlanetaService.buscar_planeta(nombre)
    if planeta:
        return jsonify({
            'id': planeta.id,
            'nombre': planeta.nombre,
            'descripcion': planeta.descripcion,
            'distancia_tierra': planeta.distancia_tierra
        })
    else:
        return jsonify({'error': f"El planeta '{nombre}' no fue encontrado."}), 404

@planetas_bp.route('/planetas/<string:nombre>', methods=['DELETE'])
def eliminar_planeta(nombre):
    """
    Elimina un planeta por su nombre.
    """
    try:
        mensaje = PlanetaService.eliminar_planeta(nombre)
        return jsonify({'message': mensaje}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
