class Nodo:
    """
    Clase Nodo para representar cada elemento del Árbol Binario de Búsqueda.
    """
    def __init__(self, nivel_poder, personaje):
        self.nivel_poder = nivel_poder
        self.personaje = personaje
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioDeBusqueda:
    """
    Clase para manejar un Árbol Binario de Búsqueda de personajes según su nivel de poder.
    """
    def __init__(self):
        self.raiz = None

    def insertar(self, nivel_poder, personaje):
        """
        Inserta un nuevo nodo en el árbol.
        :param nivel_poder: Nivel de poder del personaje
        :param personaje: Nombre del personaje
        """
        nuevo_nodo = Nodo(nivel_poder, personaje)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        """
        Inserta recursivamente un nodo en el árbol.
        """
        if nuevo_nodo.nivel_poder < nodo_actual.nivel_poder:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecho, nuevo_nodo)

    def buscar_mas_fuerte(self):
        """
        Encuentra el personaje más fuerte (nivel de poder más alto).
        :return: Nombre del personaje más fuerte
        """
        if not self.raiz:
            return None
        return self._buscar_mas_fuerte_recursivo(self.raiz)

    def _buscar_mas_fuerte_recursivo(self, nodo_actual):
        """
        Encuentra recursivamente el nodo con el nivel de poder más alto.
        """
        if nodo_actual.derecho is None:
            return nodo_actual.personaje
        return self._buscar_mas_fuerte_recursivo(nodo_actual.derecho)

    def en_orden(self):
        """
        Realiza un recorrido en orden del árbol y retorna una lista de personajes ordenados por nivel de poder.
        :return: Lista de personajes en orden ascendente de nivel de poder.
        """
        resultado = []
        self._en_orden_recursivo(self.raiz, resultado)
        return resultado

    def _en_orden_recursivo(self, nodo_actual, resultado):
        """
        Recorrido en orden recursivo.
        """
        if nodo_actual:
            self._en_orden_recursivo(nodo_actual.izquierdo, resultado)
            resultado.append((nodo_actual.personaje, nodo_actual.nivel_poder))
            self._en_orden_recursivo(nodo_actual.derecho, resultado)

# Instancia global del árbol binario
arbol_personajes = ArbolBinarioDeBusqueda()

def batalla(personaje1, personaje2):
    """
    Simula una batalla entre dos personajes, devolviendo el ganador.
    :param personaje1: Diccionario con datos del personaje 1
    :param personaje2: Diccionario con datos del personaje 2
    :return: Diccionario con datos del personaje ganador
    """
    return personaje1 if personaje1["nivel"] > personaje2["nivel"] else personaje2