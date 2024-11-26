from collections import defaultdict, deque
from app.models.habilidad import Habilidad
from config.database import db

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

class HabilidadService:
    @staticmethod
    def agregar_habilidad(nombre_habilidad, habilidad_padre=None):
        """
        Agrega una nueva habilidad y la relaciona con una habilidad padre si es proporcionada.
        :param nombre_habilidad: Nombre de la nueva habilidad.
        :param habilidad_padre: Nombre de la habilidad padre.
        """
        habilidad = Habilidad.query.filter_by(nombre=nombre_habilidad).first()
        if habilidad:
            raise ValueError(f"La habilidad '{nombre_habilidad}' ya existe.")

        habilidad_padre_obj = None
        if habilidad_padre:
            habilidad_padre_obj = Habilidad.query.filter_by(nombre=habilidad_padre).first()
            if not habilidad_padre_obj:
                raise ValueError(f"La habilidad padre '{habilidad_padre}' no existe.")

        nueva_habilidad = Habilidad(
            nombre=nombre_habilidad,
            habilidad_padre_id=habilidad_padre_obj.id if habilidad_padre_obj else None
        )

        db.session.add(nueva_habilidad)
        db.session.commit()
        return f"Habilidad '{nombre_habilidad}' agregada exitosamente."

    @staticmethod
    def mostrar_arbol():
        """
        Muestra el árbol jerárquico de habilidades.
        """
        def _recolectar_habilidades(habilidad):
            return {
                "nombre": habilidad.nombre,
                "habilidades_hijas": [
                    _recolectar_habilidades(hija) for hija in habilidad.habilidades_hijas
                ]
            }

        habilidades_raiz = Habilidad.query.filter_by(habilidad_padre_id=None).all()
        return [_recolectar_habilidades(habilidad) for habilidad in habilidades_raiz]

    @staticmethod
    def buscar_habilidad(nombre_habilidad):
        """
        Busca una habilidad por nombre.
        """
        habilidad = Habilidad.query.filter_by(nombre=nombre_habilidad).first()
        return habilidad if habilidad else None
