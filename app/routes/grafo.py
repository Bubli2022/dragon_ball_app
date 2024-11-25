from flask import Blueprint, jsonify, request
from app import universo_grafo

grafo_bp = Blueprint('grafo', __name__)

@grafo_bp.route('/grafo/planetas', methods=['POST'])
def agregar_planeta():
    """
    Agrega un planeta al grafo.
    """
    data = request.get_json()
    planeta = data.get('planeta')

    if not planeta:
        return jsonify({'error': 'Debe proporcionar el nombre del planeta.'}), 400

    universo_grafo.agregar_planeta(planeta)
    return jsonify({'message': f'Planeta {planeta} agregado al universo.'}), 201


@grafo_bp.route('/grafo/rutas', methods=['POST'])
def agregar_ruta():
    """
    Agrega una ruta entre dos planetas.
    """
    data = request.get_json()
    planeta1 = data.get('planeta1')
    planeta2 = data.get('planeta2')
    distancia = data.get('distancia')

    if not all([planeta1, planeta2, distancia]):
        return jsonify({'error': 'Debe proporcionar planeta1, planeta2 y distancia.'}), 400

    universo_grafo.agregar_ruta(planeta1, planeta2, distancia)
    return jsonify({'message': f'Ruta entre {planeta1} y {planeta2} agregada con una distancia de {distancia}.'}), 201


@grafo_bp.route('/grafo/conexiones', methods=['GET'])
def mostrar_grafo():
    """
    Muestra las conexiones del grafo.
    """
    conexiones = universo_grafo.mostrar_grafo()
    return jsonify({'conexiones': conexiones})


@grafo_bp.route('/grafo/ruta', methods=['GET'])
def obtener_ruta_mas_corta():
    """
    Calcula la ruta más corta entre dos planetas.
    """
    inicio = request.args.get('inicio')
    fin = request.args.get('fin')

    if not all([inicio, fin]):
        return jsonify({'error': 'Debe proporcionar los planetas de inicio y fin.'}), 400

    if inicio not in universo_grafo.adyacencias or fin not in universo_grafo.adyacencias:
        return jsonify({'error': 'Uno o ambos planetas no existen en el universo.'}), 404

    distancia, ruta = universo_grafo.obtener_ruta_mas_corta(inicio, fin)
    return jsonify({'distancia': distancia, 'ruta': ruta})

@grafo_bp.route('/grafo/dfs', methods=['GET'])
def buscar_dfs():
    """
    Busca un camino entre dos planetas usando DFS.
    """
    inicio = request.args.get('inicio')
    objetivo = request.args.get('objetivo')

    if not all([inicio, objetivo]):
        return jsonify({'error': 'Debe proporcionar los planetas de inicio y objetivo.'}), 400

    if inicio not in universo_grafo.adyacencias or objetivo not in universo_grafo.adyacencias:
        return jsonify({'error': 'Uno o ambos planetas no existen en el universo.'}), 404

    camino = universo_grafo.dfs(inicio, objetivo)
    if camino:
        return jsonify({'camino_dfs': camino})
    else:
        return jsonify({'error': f"No se encontró un camino de {inicio} a {objetivo}."}), 404


@grafo_bp.route('/grafo/bfs', methods=['GET'])
def buscar_bfs():
    """
    Busca el camino más corto entre dos planetas usando BFS.
    """
    inicio = request.args.get('inicio')
    objetivo = request.args.get('objetivo')

    if not all([inicio, objetivo]):
        return jsonify({'error': 'Debe proporcionar los planetas de inicio y objetivo.'}), 400

    if inicio not in universo_grafo.adyacencias or objetivo not in universo_grafo.adyacencias:
        return jsonify({'error': 'Uno o ambos planetas no existen en el universo.'}), 404

    camino = universo_grafo.bfs(inicio, objetivo)
    if camino:
        return jsonify({'camino_bfs': camino})
    else:
        return jsonify({'error': f"No se encontró un camino de {inicio} a {objetivo}."}), 404

@grafo_bp.route('/grafo/dijkstra', methods=['GET'])
def calcular_caminos_cortos():
    """
    Calcula los caminos más cortos desde un nodo inicial utilizando el algoritmo de Dijkstra.
    """
    inicio = request.args.get('inicio')

    if not inicio:
        return jsonify({'error': 'Debe proporcionar el planeta de inicio.'}), 400

    if inicio not in universo_grafo.adyacencias:
        return jsonify({'error': f"El planeta '{inicio}' no existe en el grafo."}), 404

    distancias, predecesores = universo_grafo.dijkstra(inicio)
    return jsonify({'distancias': distancias, 'predecesores': predecesores})


@grafo_bp.route('/grafo/ruta', methods=['GET'])
def reconstruir_ruta():
    """
    Reconstruye el camino más corto hacia un nodo destino.
    """
    inicio = request.args.get('inicio')
    destino = request.args.get('destino')

    if not all([inicio, destino]):
        return jsonify({'error': 'Debe proporcionar los planetas de inicio y destino.'}), 400

    if inicio not in universo_grafo.adyacencias or destino not in universo_grafo.adyacencias:
        return jsonify({'error': 'Uno o ambos planetas no existen en el grafo.'}), 404

    distancias, predecesores = universo_grafo.dijkstra(inicio)
    if destino not in distancias or distancias[destino] == float('inf'):
        return jsonify({'error': f"No se puede llegar de '{inicio}' a '{destino}'."}), 404

    camino = universo_grafo.reconstruir_camino(predecesores, destino)
    return jsonify({'camino': camino, 'distancia': distancias[destino]})
