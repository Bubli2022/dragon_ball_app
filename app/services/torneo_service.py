import heapq


class Torneo:
    """
    Clase que implementa una cola de prioridades para gestionar combates en un torneo.
    Utiliza un heap binario para priorizar a los personajes con mayor nivel de poder.
    """
    def __init__(self):
        self.cola_prioridad = []  # Heap binario (min-heap por defecto en Python)

    def agregar_personaje(self, nivel_poder, nombre):
        """
        Agrega un personaje a la cola de prioridades.
        Nota: Usamos valores negativos para convertir el min-heap en un max-heap.
        :param nivel_poder: Nivel de poder del personaje
        :param nombre: Nombre del personaje
        """
        heapq.heappush(self.cola_prioridad, (-nivel_poder, nombre))
        return f"Personaje '{nombre}' con nivel de poder {nivel_poder} agregado al torneo."

    def siguiente_enfrentamiento(self):
        """
        Extrae al personaje con mayor nivel de poder de la cola.
        :return: Tupla con el nivel de poder y el nombre del personaje
        """
        if not self.cola_prioridad:
            return None
        nivel_poder, nombre = heapq.heappop(self.cola_prioridad)
        return -nivel_poder, nombre

    def mostrar_participantes(self):
        """
        Retorna la lista de participantes en orden de prioridad.
        """
        participantes = [
            {"nombre": nombre, "nivel_poder": -nivel_poder}
            for nivel_poder, nombre in sorted(self.cola_prioridad, reverse=True)
        ]
        return participantes


