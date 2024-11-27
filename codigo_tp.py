"""
1. Grafos (Unidad 7):
Crea un grafo que represente el universo de Dragon Ball, donde los nodos
son planetas (Tierra, Namek, Vegeta) y las aristas son rutas espaciales entre
ellos. Los personajes deben poder viajar entre planetas para entrenar o
luchar.
"""

class Grafo:
    """
    Clase que representa un grafo no dirigido ponderado para modelar el universo de Dragon Ball.
    """
    def __init__(self):
        self.adyacencias = {}  # Diccionario para almacenar nodos y sus conexiones

    def agregar_planeta(self, planeta):
        """
        Agrega un nodo (planeta) al grafo.
        :param planeta: Nombre del planeta
        """
        if planeta not in self.adyacencias:
            self.adyacencias[planeta] = []

    def agregar_ruta(self, planeta1, planeta2, distancia):
        """
        Agrega una arista entre dos planetas con un peso (distancia).
        :param planeta1: Nombre del primer planeta
        :param planeta2: Nombre del segundo planeta
        :param distancia: Distancia entre los dos planetas
        """
        if planeta1 in self.adyacencias and planeta2 in self.adyacencias:
            self.adyacencias[planeta1].append((planeta2, distancia))
            self.adyacencias[planeta2].append((planeta1, distancia))  # Grafo no dirigido

    def mostrar_grafo(self):
        """
        Muestra las conexiones del grafo.
        """
        print("Conexiones del Universo de Dragon Ball:")
        for planeta, conexiones in self.adyacencias.items():
            print(f"{planeta}: {conexiones}")

    def obtener_ruta_mas_corta(self, inicio, fin):
        """
        Calcula la ruta más corta entre dos planetas usando el algoritmo de Dijkstra.
        :param inicio: Nodo de inicio
        :param fin: Nodo de destino
        :return: Distancia mínima y la ruta más corta
        """
        import heapq
        distancias = {nodo: float('inf') for nodo in self.adyacencias}
        distancias[inicio] = 0
        predecesores = {nodo: None for nodo in self.adyacencias}
        cola_prioridad = [(0, inicio)]  # (distancia acumulada, nodo actual)

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == fin:
                break

            for vecino, peso in self.adyacencias[nodo_actual]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        # Reconstruir la ruta más corta
        ruta = []
        nodo = fin
        while nodo:
            ruta.append(nodo)
            nodo = predecesores[nodo]
        ruta.reverse()

        return distancias[fin], ruta


# Pruebas básicas
if __name__ == "__main__":
    # Crear el grafo
    universo = Grafo()

    # Agregar planetas
    for planeta in ["Tierra", "Namek", "Vegeta", "Kaiosama", "Planeta Freezer"]:
        universo.agregar_planeta(planeta)

    # Agregar rutas entre planetas
    universo.agregar_ruta("Tierra", "Namek", 500)
    universo.agregar_ruta("Tierra", "Vegeta", 700)
    universo.agregar_ruta("Namek", "Kaiosama", 300)
    universo.agregar_ruta("Vegeta", "Kaiosama", 400)
    universo.agregar_ruta("Kaiosama", "Planeta Freezer", 600)

    # Mostrar el grafo
    universo.mostrar_grafo()

    # Calcular la ruta más corta
    inicio, fin = "Tierra", "Planeta Freezer"
    distancia, ruta = universo.obtener_ruta_mas_corta(inicio, fin)
    print(f"\nLa ruta más corta de {inicio} a {fin} es: {ruta} con una distancia de {distancia} unidades.")


""" 2. Recorridos DFS y BFS (Unidad 8):
o Implementa un algoritmo DFS y BFS para encontrar el camino más rápido
entre planetas, buscando a personajes que han desaparecido (como
cuando Goku viaja por el espacio para entrenar). """

from collections import deque

class Grafo:
    """
    Clase que representa un grafo no dirigido para modelar el universo de Dragon Ball.
    """
    def __init__(self):
        self.adyacencias = {}  # Diccionario para almacenar nodos y sus conexiones

    def agregar_planeta(self, planeta):
        """
        Agrega un nodo (planeta) al grafo.
        :param planeta: Nombre del planeta
        """
        if planeta not in self.adyacencias:
            self.adyacencias[planeta] = []

    def agregar_ruta(self, planeta1, planeta2):
        """
        Agrega una arista entre dos planetas.
        :param planeta1: Nombre del primer planeta
        :param planeta2: Nombre del segundo planeta
        """
        if planeta1 in self.adyacencias and planeta2 in self.adyacencias:
            self.adyacencias[planeta1].append(planeta2)
            self.adyacencias[planeta2].append(planeta1)

    def dfs(self, inicio, objetivo, visitados=None, camino=None):
        """
        Implementa un recorrido DFS para buscar un planeta objetivo.
        :param inicio: Nodo inicial
        :param objetivo: Nodo objetivo
        :param visitados: Conjunto de nodos visitados
        :param camino: Lista que representa el camino actual
        :return: Camino encontrado o None si no se encuentra
        """
        if visitados is None:
            visitados = set()
        if camino is None:
            camino = []

        visitados.add(inicio)
        camino.append(inicio)

        if inicio == objetivo:
            return camino

        for vecino in self.adyacencias[inicio]:
            if vecino not in visitados:
                resultado = self.dfs(vecino, objetivo, visitados, camino)
                if resultado:
                    return resultado

        camino.pop()  # Retrocede si no se encuentra el objetivo
        return None

    def bfs(self, inicio, objetivo):
        """
        Implementa un recorrido BFS para buscar un planeta objetivo.
        :param inicio: Nodo inicial
        :param objetivo: Nodo objetivo
        :return: Camino más corto encontrado o None si no se encuentra
        """
        visitados = set()
        cola = deque([(inicio, [inicio])])  # Cola con tuplas (nodo actual, camino hasta ese nodo)

        while cola:
            nodo_actual, camino = cola.popleft()

            if nodo_actual == objetivo:
                return camino

            visitados.add(nodo_actual)

            for vecino in self.adyacencias[nodo_actual]:
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))

        return None


# Pruebas básicas
if __name__ == "__main__":
    # Crear el grafo
    universo = Grafo()

    # Agregar planetas
    for planeta in ["Tierra", "Namek", "Vegeta", "Kaiosama", "Planeta Freezer"]:
        universo.agregar_planeta(planeta)

    # Agregar rutas entre planetas
    universo.agregar_ruta("Tierra", "Namek")
    universo.agregar_ruta("Tierra", "Vegeta")
    universo.agregar_ruta("Namek", "Kaiosama")
    universo.agregar_ruta("Vegeta", "Kaiosama")
    universo.agregar_ruta("Kaiosama", "Planeta Freezer")

    # Buscar usando DFS
    print("\nDFS - Buscando camino de 'Tierra' a 'Planeta Freezer':")
    camino_dfs = universo.dfs("Tierra", "Planeta Freezer")
    if camino_dfs:
        print(f"Camino encontrado (DFS): {camino_dfs}")
    else:
        print("No se encontró un camino.")

    # Buscar usando BFS
    print("\nBFS - Buscando camino más corto de 'Tierra' a 'Planeta Freezer':")
    camino_bfs = universo.bfs("Tierra", "Planeta Freezer")
    if camino_bfs:
        print(f"Camino encontrado (BFS): {camino_bfs}")
    else:
        print("No se encontró un camino.")


"""3. Ordenamiento Topológico (Unidad 9):
o Usa el ordenamiento topológico para planificar las etapas de
entrenamiento de un personaje. Algunas habilidades requieren dominar
otras técnicas antes de ser desbloqueadas, siguiendo una jerarquía."""

from collections import defaultdict, deque

class GrafoDirigido:
    """
    Clase que representa un grafo dirigido para modelar dependencias de habilidades.
    """
    def __init__(self):
        self.adyacencias = defaultdict(list)  # Diccionario para almacenar las conexiones dirigidas
        self.grado_entrada = defaultdict(int)  # Contador de grados de entrada para cada nodo

    def agregar_habilidad(self, habilidad):
        """
        Agrega un nodo (habilidad) al grafo.
        :param habilidad: Nombre de la habilidad
        """
        if habilidad not in self.adyacencias:
            self.adyacencias[habilidad] = []
            self.grado_entrada[habilidad] = 0

    def agregar_dependencia(self, habilidad_previa, habilidad_siguiente):
        """
        Agrega una arista dirigida entre dos habilidades.
        :param habilidad_previa: Habilidad que debe aprenderse primero
        :param habilidad_siguiente: Habilidad que depende de la previa
        """
        self.adyacencias[habilidad_previa].append(habilidad_siguiente)
        self.grado_entrada[habilidad_siguiente] += 1

    def orden_topologico(self):
        """
        Realiza un ordenamiento topológico utilizando el algoritmo de Kahn.
        :return: Lista con el orden de habilidades o None si hay un ciclo
        """
        # Cola con nodos de grado de entrada 0
        cola = deque([nodo for nodo in self.adyacencias if self.grado_entrada[nodo] == 0])
        orden = []

        while cola:
            nodo_actual = cola.popleft()
            orden.append(nodo_actual)

            # Reducir el grado de entrada de los vecinos
            for vecino in self.adyacencias[nodo_actual]:
                self.grado_entrada[vecino] -= 1
                if self.grado_entrada[vecino] == 0:
                    cola.append(vecino)

        # Verificar si todos los nodos fueron procesados
        if len(orden) == len(self.adyacencias):
            return orden
        else:
            # Hay un ciclo en el grafo
            return None


# Pruebas básicas
if __name__ == "__main__":
    # Crear el grafo
    habilidades = GrafoDirigido()

    # Agregar habilidades
    for habilidad in ["Kaioken", "Kaioken x2", "Kaioken x20", "Super Saiyajin", "Super Saiyajin 2", "Ultra Instinto"]:
        habilidades.agregar_habilidad(habilidad)

    # Agregar dependencias
    habilidades.agregar_dependencia("Kaioken", "Kaioken x2")
    habilidades.agregar_dependencia("Kaioken x2", "Kaioken x20")
    habilidades.agregar_dependencia("Kaioken x2", "Super Saiyajin")
    habilidades.agregar_dependencia("Super Saiyajin", "Super Saiyajin 2")
    habilidades.agregar_dependencia("Super Saiyajin 2", "Ultra Instinto")

    # Realizar el ordenamiento topológico
    print("\nOrdenamiento Topológico:")
    orden = habilidades.orden_topologico()
    if orden:
        print(f"Orden de entrenamiento: {orden}")
    else:
        print("Error: Hay un ciclo en las dependencias de habilidades.")

"""4. Problemas NP y Camino Mínimo (Unidad 10):
o Aplica el problema del camino mínimo utilizando Dijkstra para encontrar la
mejor ruta en el mapa del universo de Dragon Ball para recolectar las
Esferas del Dragón lo más rápido posible.
"""

import heapq

class Grafo:
    """
    Clase que representa un grafo ponderado no dirigido para modelar el universo de Dragon Ball.
    """
    def __init__(self):
        self.adyacencias = {}  # Diccionario para almacenar nodos y sus conexiones

    def agregar_planeta(self, planeta):
        """
        Agrega un nodo (planeta) al grafo.
        :param planeta: Nombre del planeta
        """
        if planeta not in self.adyacencias:
            self.adyacencias[planeta] = []

    def agregar_ruta(self, planeta1, planeta2, peso):
        """
        Agrega una arista ponderada entre dos planetas.
        :param planeta1: Nombre del primer planeta
        :param planeta2: Nombre del segundo planeta
        :param peso: Distancia o tiempo entre los dos planetas
        """
        self.adyacencias[planeta1].append((planeta2, peso))
        self.adyacencias[planeta2].append((planeta1, peso))

    def dijkstra(self, inicio):
        """
        Implementa el algoritmo de Dijkstra para encontrar el camino más corto desde un nodo inicial.
        :param inicio: Nodo inicial (planeta de partida)
        :return: Diccionarios con las distancias mínimas y los predecesores
        """
        distancias = {nodo: float('inf') for nodo in self.adyacencias}
        distancias[inicio] = 0
        predecesores = {nodo: None for nodo in self.adyacencias}
        cola_prioridad = [(0, inicio)]  # (distancia acumulada, nodo actual)

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            # Explorar los vecinos del nodo actual
            for vecino, peso in self.adyacencias[nodo_actual]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return distancias, predecesores

    def reconstruir_camino(self, predecesores, destino):
        """
        Reconstruye el camino más corto desde el nodo inicial hasta un nodo de destino.
        :param predecesores: Diccionario de predecesores generado por Dijkstra
        :param destino: Nodo final
        :return: Lista con el camino más corto
        """
        camino = []
        nodo = destino
        while nodo:
            camino.append(nodo)
            nodo = predecesores[nodo]
        return camino[::-1]


# Pruebas básicas
if __name__ == "__main__":
    # Crear el grafo
    universo = Grafo()

    # Agregar planetas
    for planeta in ["Tierra", "Namek", "Vegeta", "Kaiosama", "Planeta Freezer", "Nuevo Namek"]:
        universo.agregar_planeta(planeta)

    # Agregar rutas entre planetas
    universo.agregar_ruta("Tierra", "Namek", 500)
    universo.agregar_ruta("Tierra", "Vegeta", 700)
    universo.agregar_ruta("Namek", "Kaiosama", 300)
    universo.agregar_ruta("Vegeta", "Kaiosama", 400)
    universo.agregar_ruta("Kaiosama", "Planeta Freezer", 600)
    universo.agregar_ruta("Namek", "Nuevo Namek", 200)

    # Calcular caminos más cortos desde "Tierra"
    print("\nCalculando caminos más cortos desde 'Tierra':")
    distancias, predecesores = universo.dijkstra("Tierra")

    for planeta, distancia in distancias.items():
        print(f"Distancia a {planeta}: {distancia} unidades")

    # Reconstruir camino más corto hacia "Planeta Freezer"
    destino = "Planeta Freezer"
    camino = universo.reconstruir_camino(predecesores, destino)
    print(f"\nEl camino más corto hacia {destino} es: {camino} con una distancia de {distancias[destino]} unidades.")
