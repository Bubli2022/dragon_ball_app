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
