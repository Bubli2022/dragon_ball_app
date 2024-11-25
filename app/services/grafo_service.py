import heapq
from collections import deque

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

    def mostrar_grafo(self):
        """
        Retorna las conexiones del grafo como un diccionario.
        """
        return self.adyacencias

    def obtener_ruta_mas_corta(self, inicio, fin):
        """
        Calcula la ruta más corta entre dos planetas usando el algoritmo de Dijkstra.
        :param inicio: Nodo de inicio
        :param fin: Nodo de destino
        :return: Distancia mínima y la ruta más corta
        """
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
