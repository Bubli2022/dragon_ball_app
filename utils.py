import time

def medir_tiempo(funcion, *args, **kwargs):
    """
    Mide el tiempo de ejecución de una función.
    :param funcion: Función a medir
    :param args: Argumentos posicionales de la función
    :param kwargs: Argumentos de palabras clave de la función
    :return: Resultado de la función
    """
    inicio = time.time()
    resultado = funcion(*args, **kwargs)
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    return resultado
