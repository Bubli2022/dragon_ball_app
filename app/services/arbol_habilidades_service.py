class NodoHabilidad:
    """
    Representa un nodo en el árbol general de habilidades.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        """
        Agrega un nodo hijo al nodo actual.
        :param nodo_hijo: Instancia de NodoHabilidad
        """
        self.hijos.append(nodo_hijo)

    def __str__(self):
        """
        Representación textual del nodo.
        """
        return self.nombre


class ArbolHabilidades:
    """
    Representa el árbol general de habilidades de un personaje.
    """
    def __init__(self, habilidad_raiz):
        """
        Inicializa el árbol con una habilidad raíz.
        :param habilidad_raiz: Nombre de la habilidad raíz
        """
        self.raiz = NodoHabilidad(habilidad_raiz)

    def mostrar_arbol(self, nodo=None, nivel=0):
        """
        Retorna el árbol completo en formato jerárquico.
        :param nodo: Nodo actual (inicia con la raíz)
        :param nivel: Nivel de profundidad del nodo (para formato)
        """
        if nodo is None:
            nodo = self.raiz

        arbol = "  " * nivel + f"- {nodo.nombre}\n"
        for hijo in nodo.hijos:
            arbol += self.mostrar_arbol(hijo, nivel + 1)
        return arbol

    def buscar_habilidad(self, nodo, habilidad):
        """
        Busca una habilidad en el árbol.
        :param nodo: Nodo actual
        :param habilidad: Nombre de la habilidad a buscar
        :return: Nodo encontrado o None si no existe
        """
        if nodo is None:
            return None

        if nodo.nombre == habilidad:
            return nodo

        for hijo in nodo.hijos:
            resultado = self.buscar_habilidad(hijo, habilidad)
            if resultado:
                return resultado

        return None

    def agregar_habilidad(self, nombre_habilidad, habilidad_padre):
        """
        Agrega una nueva habilidad al árbol como hija de una habilidad existente.
        :param nombre_habilidad: Nombre de la nueva habilidad
        :param habilidad_padre: Nombre de la habilidad padre
        """
        nodo_padre = self.buscar_habilidad(self.raiz, habilidad_padre)
        if nodo_padre:
            nodo_padre.agregar_hijo(NodoHabilidad(nombre_habilidad))
            return f"Habilidad '{nombre_habilidad}' agregada como mejora de '{habilidad_padre}'."
        else:
            return f"Habilidad padre '{habilidad_padre}' no encontrada."

# Instancia global del árbol de habilidades
arbol_habilidades = ArbolHabilidades("Kamehameha")