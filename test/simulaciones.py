from app.services.evolucion_service import calcular_evolucion_poder
from app.services.arbol_service import ArbolBinarioDeBusqueda
from app.services.torneo_service import Torneo
from utils import medir_tiempo
from random import randint


# Simulación: Evolución de poder
def prueba_evolucion():
    medir_tiempo(calcular_evolucion_poder, 1000, [1.5, 2, 1.2])


# Simulación: Árbol Binario de Búsqueda
def prueba_arbol_binario():
    arbol = ArbolBinarioDeBusqueda()
    medir_tiempo(lambda: [arbol.insertar(randint(1, 10000), f"Personaje {i}") for i in range(1000)])
    print("Personajes insertados en el árbol.")


# Simulación: Gestión de Torneos
def prueba_torneo():
    torneo = Torneo()
    participantes = [{"nombre": f"Personaje {i}", "nivel": randint(1, 10000)} for i in range(1000)]
    for p in participantes:
        torneo.agregar_personaje(p["nivel"], p["nombre"])
    medir_tiempo(lambda: torneo.mostrar_participantes())
    medir_tiempo(lambda: [torneo.siguiente_enfrentamiento() for _ in range(len(participantes))])


if __name__ == "__main__":
    print("\n--- Prueba: Evolución Recursiva ---")
    prueba_evolucion()

    print("\n--- Prueba: Árbol Binario ---")
    prueba_arbol_binario()

    print("\n--- Prueba: Torneo ---")
    prueba_torneo()
