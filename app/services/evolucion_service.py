def calcular_evolucion_poder(nivel_poder_inicial, multiplicadores, indice=0):
    """
    Calcula recursivamente el nivel de poder final de un personaje tras aplicar una serie de multiplicadores.

    :param nivel_poder_inicial: Nivel de poder inicial del personaje.
    :param multiplicadores: Lista de multiplicadores (por ejemplo, [1.5, 2, 1.2]).
    :param indice: Índice del multiplicador actual a aplicar (inicia en 0).
    :return: Nivel de poder final tras aplicar todos los multiplicadores.
    """
    # Caso base: si no hay más multiplicadores que aplicar, devolver el nivel de poder actual
    if indice >= len(multiplicadores):
        return nivel_poder_inicial

    # Aplicar el multiplicador actual al nivel de poder
    nuevo_nivel_poder = nivel_poder_inicial * multiplicadores[indice]

    # Llamada recursiva para el siguiente multiplicador
    return calcular_evolucion_poder(nuevo_nivel_poder, multiplicadores, indice + 1)
