Universidad de almirante Brown
Tecnicatura en programación
Estructura de datos
2do cuatrimestre 2024
—------------------------------------------------------------------------------------------------------------
Trabajo final: “Juego de Dragon Ball”
Integrantes:
Gianfranco Falcucci
Ariel marcos Perez
Valentina Horociuk  
LINK DEL REPO EN GitHub:
https://github.com/Bubli2022/dragon_ball_app/tree/main
—--------------------------------------------------------------------------------------------------------------
Indice

1. Introducción
2. Objetivos del trabajo
3. Documentación por fases del desarrollo  
   Fase 1 : Planificación
   Fase 2 : Análisis
   Fase 3 : Diseño
   Fase 4 : Desarrollo
   Fase 5 : Pruebas
   Fase 6 : Implementación
   Fase 7: Mantenimiento

4. Parte teórica y realización de pruebas
   Clases e interface
   Estructuras recursivas
   Arboles binarios y generales
   Cola de prioridades y heap binaria
   Analisis de algoritmo

5. Parte de codificación y algoritmos
   Grafos recorrido de DFS Y BFS
   Ordenamiento topológico, problemas NP y comino mínimo
6. Conclusión
7. Anexos
   Documentos visuales complementarios
   Diagrama de clases , flujos y diseño arquitectónico

Nuestro grupo de trabajo del proyecto Juego de Dragon Ball conformado por Gianfranco Falcucci, Ariel marcos Perez y Valentina Horociuk iniciamos con una presentación personal, compartiendo nuestras experiencias y discutimos las consignas del proyecto, realizamos reuniones semanales, en ellas fuimos estableciendo las pautas de desarrollo a fin de llegar a este trabajo final.
Decidimos hacer un juego de Dragon Ball porque puede ser una forma de rendir un homenaje a la serie, recrear momentos favoritos y explorar nuevas historias o mecánicas inspiradas en su universo.
Este juego podría aplicar funcionamientos como:

1. Combates dinámicos: llevar a cabo sistemas de lucha fluidos en 2D O 3D.
2. Poderes especiales: simular efectos visuales y procesos únicos como el kamehameha o la teletransportación
3. Mundos abiertos: realizar escenarios interactivos donde los jugadores exploren ubicaciones icónicas como namek o la torre de karin.
4. Además, este proyecto permitiría imaginar nuevas fusiones, sagas alternativas, convertir el juego en un RPG o un simulador estratégico.

Parte 1: Teoría y Realización Práctica

1. Desarrollo de Clases e Interfaces (Unidad 1):
   Nuestro grupo eligió diseñar una clase principal Personaje que encapsule los atributos esenciales para un sistema de juego de Dragon Ball. Este diseño se basa en la modularidad y la claridad, asegurando que cada aspecto del personaje esté bien definido y sea fácil de manipular mediante métodos y estructuras de datos eficientes.
   Además, implementamos interfaces para manejar acciones comunes como gestionar combates, subir de nivel y adquirir habilidades. Estas interfaces nos permiten abstraer las acciones y mantener la flexibilidad para futuros cambios o expansiones en el juego. Por ejemplo:
   • Gestión de Combates: Facilita la ejecución de una batalla entre dos personajes, evaluando sus niveles de poder y habilidades.
   • Subida de Nivel: Proporciona métodos para incrementar atributos clave de un personaje tras completar misiones o combates.
   • Adquisición de Habilidades: Permite agregar nuevas habilidades, organizándolas en una estructura que garantiza eficiencia en búsquedas y consultas.
   Elegimos esta estructura porque mejora la experiencia del jugador al proporcionar interacciones rápidas y un código que es fácil de mantener y escalar. Al implementar buenas prácticas como encapsulación y uso de interfaces, aseguramos que las funcionalidades estén separadas y bien definidas, evitando complejidades innecesarias.
   Explicación del Código
1. Clase Personaje:
   Creamos esta clase para encapsular todos los atributos esenciales de un personaje. Al usar un método **str**, facilitamos la visualización de la información del personaje en el juego.
1. Interfaces:
   o GestionCombates se encarga de ejecutar combates comparando los niveles de poder. Optamos por usar un método estático porque las acciones no dependen del estado interno de una instancia de la interfaz.
   o SubidaNivel y GestionHabilidades permiten aumentar el nivel de poder y agregar habilidades, asegurando un sistema modular y reutilizable.
1. Modularidad y Expansión:
   La implementación de interfaces separadas asegura que cada funcionalidad esté desacoplada. Esto facilita futuras expansiones del juego, como la introducción de nuevos tipos de habilidades o ajustes en las mecánicas de combate.
1. Buenas Prácticas:
   o Uso de documentación en los métodos.
   o Métodos reutilizables, como el de aprender_habilidad, que evita duplicados al agregar habilidades.
   Este diseño mejora la fluidez del juego porque organiza y optimiza la lógica en segmentos manejables y personalizables.

1. Estructuras Recursivas (Unidad 2):
   Para esta sección, diseñamos un algoritmo recursivo que permite calcular la evolución del nivel de poder de un personaje tras cada combate, aplicando multiplicadores derivados de transformaciones como Super Saiyajin o Kaioken. Elegimos una solución recursiva porque este enfoque permite modelar el proceso incremental de los combates de manera natural, especialmente cuando hay varias transformaciones aplicadas consecutivamente.
   La recursión nos ofrece las siguientes ventajas:
1. Claridad Conceptual: Cada llamada recursiva representa un combate, lo que facilita visualizar la secuencia de transformaciones y el efecto acumulativo de los multiplicadores.
1. Simplicidad del Código: La lógica del cálculo se reduce a unas pocas líneas, eliminando la necesidad de estructuras iterativas más complejas.
1. Modularidad: Podemos integrar fácilmente nuevos multiplicadores o reglas de transformación sin modificar la estructura general del algoritmo.
   Desde el punto de vista del usuario, esta solución mejora la interfaz del juego porque permite que las transformaciones sean procesadas dinámicamente, mostrando al jugador cómo su nivel de poder se incrementa tras cada combate. Además, los multiplicadores pueden ser personalizados, ofreciendo una experiencia de juego más inmersiva.
   En términos de rendimiento, aseguramos que el algoritmo sea eficiente al limitar la profundidad de las llamadas recursivas al número de combates realizados, lo que es manejable dentro de las limitaciones de Python. También se incluyeron casos base para evitar recursiones infinitas y garantizar una ejecución controlada.
   Explicación del Código
1. Parámetros del Algoritmo:
   o nivel_poder_inicial: Representa el nivel de poder del personaje antes de aplicar los multiplicadores.
   o multiplicadores: Es una lista de factores que representan las transformaciones (ejemplo: Kaioken x1.5 o Super Saiyajin x2).
   o indice: Controla qué multiplicador se aplica en cada llamada recursiva.
1. Caso Base:
   Si el índice actual supera el tamaño de la lista de multiplicadores, la recursión termina y devuelve el nivel de poder calculado hasta el momento. Esto asegura que no haya recursiones infinitas.
1. Llamada Recursiva:
   En cada iteración, se aplica el multiplicador actual al nivel de poder y se realiza una llamada recursiva con el siguiente índice. Esto asegura que cada transformación se procese en el orden correcto.

1. Árboles Binarios (Unidad 3):
   En nuestro trabajo, optamos por usar un Árbol Binario de Búsqueda (ABB) para organizar los personajes según su nivel de poder. Esta estructura fue seleccionada porque permite:
1. Búsqueda Rápida: En un ABB, la búsqueda de elementos (como el personaje más fuerte o el más débil) tiene una complejidad promedio de O(log⁡n)O(\log n)O(logn), lo que hace que las consultas sean rápidas incluso con un gran número de personajes.
1. Inserción Eficiente: Cada nuevo personaje se puede insertar en tiempo O(log⁡n)O(\log n)O(logn), siempre y cuando el árbol esté balanceado.
1. Ordenación Natural: Los elementos en un ABB están organizados automáticamente de forma que los valores menores se encuentran en el subárbol izquierdo y los valores mayores en el derecho. Esto facilita la identificación del personaje más fuerte (ubicado en el nodo más a la derecha).
   Desde el punto de vista del jugador, esta implementación mejora la interfaz del juego al permitir:
   • Selección eficiente de los rivales más fuertes: Enfrentar al personaje con mayor nivel de poder en un torneo o combate.
   • Flexibilidad: Se pueden añadir personajes dinámicamente sin necesidad de reordenar toda la lista de niveles de poder.
   • Escalabilidad: A medida que el juego crece, esta estructura sigue siendo eficiente y no se ve afectada por un gran número de personajes.
   Además, consideramos que el uso de un ABB refleja los conceptos aprendidos en la materia, integrando estructuras eficientes y adaptadas a los requisitos del problema.
   Explicación del Código
1. Clase Nodo:
   Cada nodo del árbol almacena el nivel de poder y el nombre del personaje, además de los punteros a los nodos izquierdo y derecho.
1. Clase ArbolBinarioDeBusqueda:
   Esta clase maneja todas las operaciones relacionadas con el árbol, como insertar nodos, buscar el personaje más fuerte y recorrer el árbol en orden ascendente.
1. Operaciones Principales:
   o Inserción: Se realiza de forma recursiva, comparando el nivel de poder del nuevo personaje con el nodo actual para determinar si debe ir al subárbol izquierdo o derecho.
   o Búsqueda del Más Fuerte: Recorremos siempre hacia el nodo más a la derecha del árbol, ya que este contiene el nivel de poder más alto en un ABB.
   o Recorrido en Orden: Genera una lista de personajes ordenados de menor a mayor nivel de poder, lo que puede ser útil para mostrar clasificaciones en el juego.
1. Pruebas:
   o Insertamos personajes como Goku, Vegeta y Broly con diferentes niveles de poder.
   o Verificamos que el árbol encuentra correctamente al personaje más fuerte ("Broly") y genera la lista ordenada de niveles de poder.

1. Árboles Generales (Unidad 4):
   En esta sección, utilizamos un Árbol General para modelar el sistema de habilidades de los personajes en el juego de Dragon Ball. Cada nodo representa una habilidad específica, mientras que sus hijos representan las transformaciones o mejoras que se derivan de esa habilidad. Por ejemplo:
   • El nodo "Kamehameha" tiene como hijos "Kamehameha x10" y "Kamehameha Definitivo".
   • De forma similar, "Kaioken" puede tener hijos como "Kaioken x2" o "Kaioken x20".
   Elegimos esta estructura por varias razones:
1. Flexibilidad en la Representación: Un Árbol General permite que cada nodo tenga un número variable de hijos, lo cual es ideal para representar habilidades que pueden tener múltiples derivaciones o mejoras.
1. Organización Jerárquica: El árbol refleja de manera intuitiva la progresión de habilidades, mostrando claramente qué transformaciones dependen de habilidades base.
1. Búsquedas y Navegación Eficientes: Con recorridos en profundidad o amplitud, podemos encontrar rápidamente si un personaje tiene una habilidad específica o listar todas las mejoras derivadas de una técnica.
1. Interfaz Mejorada para el Usuario: Para el jugador, esta estructura permite visualizar de manera clara las técnicas disponibles y sus posibles evoluciones, mejorando la experiencia de juego y la planificación estratégica.
   Desde el punto de vista técnico, el Árbol General proporciona una solución escalable, ya que se puede extender fácilmente a medida que se agreguen nuevas habilidades o transformaciones. Además, esta estructura está alineada con los conceptos vistos en la materia, como la representación jerárquica de datos y los recorridos de árboles.
   Explicación del Código
1. Clase NodoHabilidad:
   Representa cada habilidad del personaje. Cada nodo puede tener una cantidad variable de hijos, lo que permite modelar fácilmente las transformaciones derivadas.
1. Clase ArbolHabilidades:
   Maneja el árbol general. Ofrece funcionalidades para:
   o Agregar habilidades: Permite añadir nuevas técnicas como mejoras de una habilidad existente.
   o Buscar habilidades: Realiza una búsqueda en profundidad para encontrar un nodo por su nombre.
   o Mostrar el árbol: Recorre el árbol y presenta las habilidades de manera jerárquica, facilitando su visualización.
1. Operaciones Básicas:
   o Creamos un árbol inicial con la habilidad raíz ("Kamehameha").
   o Agregamos derivaciones como "Kamehameha x10" y "Kamehameha Definitivo".
   o Mostramos la estructura completa del árbol en un formato jerárquico.
   o Buscamos habilidades específicas para verificar su existencia y ubicación.
   Pruebas:
   El programa muestra correctamente las habilidades en una estructura jerárquica y permite buscar y agregar habilidades dinámicamente.

1. Cola de Prioridades y Heap Binaria (Unidad 5):
   Para esta sección, decidimos implementar una cola de prioridades utilizando una heap binaria para gestionar los enfrentamientos en un torneo. Esta estructura nos permite organizar los personajes de manera que aquellos con el nivel de poder más alto tengan prioridad en los combates.
   Optamos por usar una cola de prioridades basada en un heap binario por las siguientes razones:
1. Eficiencia:
   o La inserción y extracción de elementos en una cola de prioridades basada en heap tienen una complejidad de O(log⁡n)O(\log n)O(logn), lo cual es ideal para manejar un gran número de personajes.
   o Esto garantiza que el sistema pueda gestionar torneos grandes sin afectar el rendimiento.
1. Orden Dinámico:
   o La cola reorganiza automáticamente a los personajes según su nivel de poder cada vez que se realiza una operación de inserción o extracción. Esto asegura que siempre podamos acceder al personaje más fuerte en tiempo O(1)O(1)O(1).
1. Aplicación en Torneos:
   o En un torneo, es crucial que los enfrentamientos sean justos y emocionantes. Al priorizar a los personajes más fuertes, el sistema puede organizar combates donde los participantes tengan habilidades similares o donde los más fuertes lideren las primeras rondas.
1. Interfaz Mejorada para el Usuario:
   o Para el jugador, esta implementación permite una visualización clara de los participantes del torneo, destacando quién tiene mayor prioridad para los enfrentamientos.
   En resumen, esta estructura no solo mejora la fluidez del sistema, sino que también es escalable y está alineada con los conceptos aprendidos en la materia, como el manejo eficiente de datos mediante estructuras avanzadas.
   Explicación del Código
1. Clase Torneo:
   o Implementamos una cola de prioridades utilizando el módulo heapq de Python, que por defecto maneja un min-heap.
   o Para convertirlo en un max-heap, almacenamos los niveles de poder como negativos al insertar en la cola, y los restauramos a positivos al extraer.
1. Operaciones Principales:
   o Agregar personajes:
   Los personajes se añaden a la cola junto con su nivel de poder. Gracias a la estructura del heap, la cola se reorganiza automáticamente para mantener al personaje más fuerte al frente.
   o Siguiente enfrentamiento:
   Extraemos al personaje con el mayor nivel de poder para participar en el próximo combate. Esta operación se realiza en O(log⁡n)O(\log n)O(logn).
   o Mostrar participantes:
   Ordenamos y listamos a los personajes según su prioridad actual en la cola, facilitando la visualización del torneo.
1. Pruebas:
   o Se agregaron personajes como Goku, Vegeta y Broly con diferentes niveles de poder.
   o El sistema seleccionó correctamente al personaje más fuerte (Goku, con nivel de poder 9000) para el primer combate, seguido por Vegeta y los demás en orden decreciente.

1. Análisis de Algoritmos (Unidad 6):
   En esta sección, analizamos la eficiencia de los algoritmos implementados en el proyecto para las batallas, la evolución de poder y la organización de los personajes. Evaluamos su complejidad temporal y espacial, justificando por qué las estructuras elegidas mejoran la fluidez del juego y optimizan la experiencia del usuario.
1. Batallas: Gestión con Comparación Directa
   Para las batallas, utilizamos una comparación directa entre los niveles de poder de dos personajes. Este enfoque tiene una complejidad de O(1)O(1)O(1), ya que solo involucra una operación de comparación sin depender del tamaño de los datos.
   • Ventajas:
   o Es simple y rápido, adecuado para escenarios donde solo se necesita decidir el ganador de una batalla.
   o No requiere estructuras adicionales, optimizando el uso de memoria (O(1)O(1)O(1)).
   • Limitaciones:
   o No es escalable si queremos gestionar múltiples batallas simultáneamente.
   o Para resolver esta limitación, se complementa con la cola de prioridades en los torneos.
1. Evolución de Poder: Algoritmo Recursivo
   Para calcular la evolución del nivel de poder tras las transformaciones, usamos un algoritmo recursivo que aplica multiplicadores en cascada.
   • Complejidad Temporal:
   o En el peor caso, el algoritmo realiza nnn llamadas recursivas, donde nnn es el número de multiplicadores, con una complejidad de O(n)O(n)O(n).
   • Complejidad Espacial:
   o En términos de espacio, la pila de llamadas ocupa O(n)O(n)O(n), lo que podría ser un factor limitante si nnn es muy grande. Sin embargo, para escenarios de juego, el número de multiplicadores suele ser bajo, lo que hace que esta solución sea viable.
   • Ventajas:
   o Permite una implementación limpia y clara, representando de manera natural el proceso de evolución en cascada.
   o Mejora la experiencia del usuario al reflejar de forma lógica y progresiva cómo cambian los niveles de poder.
1. Organización de Personajes: Árbol Binario de Búsqueda
   Para organizar a los personajes según su nivel de poder, usamos un Árbol Binario de Búsqueda (ABB).
   • Complejidad Temporal:
   o Inserción: O(log⁡n)O(\log n)O(logn) en un árbol balanceado, ya que solo recorremos una rama del árbol.
   o Búsqueda del personaje más fuerte: También O(log⁡n)O(\log n)O(logn), ya que se accede directamente al nodo más a la derecha.
   o En el peor caso (si el árbol está desbalanceado), ambas operaciones pueden ser O(n)O(n)O(n).
   • Complejidad Espacial:
   o El ABB requiere O(n)O(n)O(n) para almacenar nnn personajes, con un nodo para cada uno.
   • Ventajas:
   o Es una solución escalable que asegura búsquedas e inserciones rápidas para gestionar muchos personajes.
   o Permite listar a los personajes en orden, lo que facilita la visualización del ranking por poder.
1. Gestión de Torneos: Cola de Prioridades con Heap Binario
   Para los torneos, usamos una cola de prioridades implementada con un heap binario.
   • Complejidad Temporal:
   o Inserción: O(log⁡n)O(\log n)O(logn) por operación.
   o Extracción del más fuerte: O(log⁡n)O(\log n)O(logn) al reorganizar el heap.
   o Las operaciones son eficientes incluso con un gran número de personajes.
   • Complejidad Espacial:
   o Requiere O(n)O(n)O(n) para almacenar los personajes en el heap.
   • Ventajas:
   o Garantiza que siempre tengamos acceso rápido al personaje con mayor prioridad (nivel de poder más alto).
   o Mejora la fluidez del torneo al automatizar la gestión de combates.

Resumen Comparativo
Funcionalidad Estructura Usada Complejidad Temporal Complejidad Espacial Ventajas Clave
Batallas Comparación directa O(1)O(1)O(1) O(1)O(1)O(1) Simplicidad y rapidez en enfrentamientos individuales.
Evolución de Poder Recursión O(n)O(n)O(n) O(n)O(n)O(n) Representación natural de transformaciones.
Organización de Datos Árbol Binario de Búsqueda O(log⁡n)O(\log n)O(logn)\* O(n)O(n)O(n) Búsqueda e inserción eficientes, escalabilidad.
Gestión de Torneos Cola de Prioridades (Heap) O(log⁡n)O(\log n)O(logn) O(n)O(n)O(n) Priorización automática, ideal para torneos grandes.

-  O(log⁡n)O(\log n)O(logn) en ABB balanceado; O(n)O(n)O(n) en peor caso desbalanceado.

Parte 2: Codificación y Algoritmos

1. Grafos (Unidad 7):
   Representación del Universo como un Grafo
   Para modelar el universo de Dragon Ball, optamos por usar un grafo no dirigido ponderado, donde:
   • Nodos: Representan los planetas del universo (por ejemplo, Tierra, Namek, Vegeta, etc.).
   • Aristas: Representan rutas espaciales entre los planetas.
   • Pesos: Representan la distancia o tiempo necesario para viajar entre dos planetas.
   Esta estructura es ideal porque:
1. Flexibilidad: Permite representar eficientemente las conexiones entre planetas. Si se agregan nuevos planetas o rutas, es fácil actualizar el grafo.
1. Gestión de Rutas: Podemos usar algoritmos de grafos (como Dijkstra o Floyd-Warshall) para calcular la ruta más corta entre dos planetas, mejorando la experiencia de juego al optimizar viajes para entrenamiento o combate.
1. Escalabilidad: A medida que el universo crece (nuevos planetas o galaxias), el modelo sigue siendo eficiente y fácil de mantener.
   Fluidez para el Usuario
   Desde el punto de vista del jugador:
   • Esta implementación mejora la interfaz al permitirles elegir rutas basadas en distancia o tiempo de viaje.
   • Los jugadores pueden planificar estrategias, como entrenar en un planeta lejano con beneficios específicos o viajar rápidamente a un lugar para recolectar las Esferas del Dragón.

CÓDIGO IMPLEMENTADO
class Grafo:
"""
Clase que representa un grafo no dirigido ponderado para modelar el universo de Dragon Ball.
"""
def **init**(self):
self.adyacencias = {} # Diccionario para almacenar nodos y sus conexiones

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

if **name** == "**main**": # Crear el grafo
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

Explicación del Código

1. Clase Grafo:
   o Representa el universo como un grafo no dirigido ponderado.
   o Utiliza un diccionario para almacenar los nodos (planetas) y sus conexiones (rutas espaciales).
2. Métodos Principales:
   o agregar_planeta: Añade nodos al grafo.
   o agregar_ruta: Crea aristas ponderadas entre planetas.
   o mostrar_grafo: Imprime las conexiones del grafo, útil para verificar su estructura.
   o obtener_ruta_mas_corta: Implementa el algoritmo de Dijkstra para calcular la ruta más corta entre dos planetas.
3. Pruebas:
   o Creamos planetas y rutas entre ellos, incluyendo distancias.
   o Calculamos la ruta más corta desde "Tierra" a "Planeta Freezer". El programa devuelve tanto la distancia mínima como la secuencia de planetas a recorrer.
4. Recorridos DFS y BFS (Unidad 8):
   Uso de Algoritmos DFS y BFS
   Para resolver el problema de buscar a personajes desaparecidos en el universo de Dragon Ball, implementamos los algoritmos DFS (Depth-First Search) y BFS (Breadth-First Search). Ambos son adecuados para recorrer un grafo y buscar un nodo objetivo, pero tienen diferencias clave que influyen en su selección según el escenario:
5. DFS (Depth-First Search):
   o Realiza un recorrido en profundidad, explorando cada ruta hasta el final antes de retroceder y buscar otras alternativas.
   o Es ideal para escenarios donde buscamos caminos largos o queremos explorar rutas específicas, como en áreas menos conectadas del universo.
6. BFS (Breadth-First Search):
   o Realiza un recorrido en amplitud, explorando todos los vecinos de un nodo antes de avanzar.
   o Es más adecuado para encontrar el camino más corto en términos de número de aristas, como cuando un personaje desaparecido está cerca del punto de partida.
   Ventajas para el Usuario
   Desde el punto de vista del jugador, ambos algoritmos mejoran la interfaz y la jugabilidad:
   • DFS: Permite explorar rutas largas y profundas, lo que puede ser útil para misiones de exploración o entrenamiento en planetas lejanos.
   • BFS: Proporciona una solución rápida para encontrar a personajes cercanos, optimizando el tiempo de respuesta del jugador.
   Ambos algoritmos garantizan una búsqueda completa en el grafo, asegurando que ningún planeta quede sin explorar.

CÓDIGO IMPLEMENTADO

from collections import deque

class Grafo:
"""
Clase que representa un grafo no dirigido para modelar el universo de Dragon Ball.
"""
def **init**(self):
self.adyacencias = {} # Diccionario para almacenar nodos y sus conexiones

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

if **name** == "**main**": # Crear el grafo
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

Explicación del Código

1. Clase Grafo:
   o Representa un grafo no dirigido, donde los nodos son planetas y las aristas son las rutas entre ellos.
   o Se usa un diccionario para almacenar las conexiones de cada planeta.
2. Métodos de Búsqueda:
   o DFS:
    Utiliza recursión para explorar en profundidad.
    Mantiene un conjunto de planetas visitados y una lista para almacenar el camino actual.
    Si no encuentra el objetivo en un camino, retrocede (backtracking).
   o BFS:
    Utiliza una cola para explorar los nodos en amplitud.
    Devuelve el camino más corto en términos de número de aristas.
3. Pruebas:
   o Se construyó un grafo con planetas y rutas espaciales.
   o Se probó la búsqueda desde "Tierra" hasta "Planeta Freezer" usando ambos algoritmos:
    DFS: Encontró un camino explorando en profundidad.
    BFS: Encontró el camino más corto en términos de pasos.
4. Ordenamiento Topológico (Unidad 9):
   Uso de Ordenamiento Topológico para Planificar Entrenamientos
   Para planificar las etapas de entrenamiento de un personaje en Dragon Ball, utilizamos el ordenamiento topológico aplicado a un grafo dirigido acíclico (DAG). En este contexto:
   • Nodos: Representan las habilidades o técnicas que el personaje puede aprender (por ejemplo, "Kaioken", "Kaioken x2", "Super Saiyajin").
   • Aristas dirigidas: Representan las dependencias entre habilidades, indicando que una técnica debe dominarse antes de desbloquear otra.
   Por qué Elegimos el Ordenamiento Topológico
5. Gestión de Dependencias:
   o El ordenamiento topológico asegura que las técnicas sean aprendidas en el orden correcto, respetando las dependencias definidas.
   o Por ejemplo, un personaje no puede aprender "Kaioken x20" antes de dominar "Kaioken x2".
6. Eficiencia y Escalabilidad:
   o Este enfoque es eficiente (O(V+E)O(V + E)O(V+E), donde VVV es el número de habilidades y EEE el número de dependencias).
   o Escalable a medida que se añaden nuevas habilidades o jerarquías más complejas al sistema de entrenamiento.
7. Fluidez para el Usuario:
   o Desde el punto de vista del jugador, este sistema permite visualizar claramente las etapas de entrenamiento, mostrando qué habilidades deben desbloquearse antes de avanzar.
   o Mejora la experiencia del jugador al proporcionar una guía estructurada del progreso.
   Beneficios Adicionales
   • Facilita la planificación estratégica en el juego, permitiendo a los jugadores optimizar su tiempo y recursos al entrenar.
   • Es una representación intuitiva de las jerarquías de aprendizaje en el universo de Dragon Ball.

CÓDIGO IMPLEMENTADO

from collections import defaultdict, deque

class GrafoDirigido:
"""
Clase que representa un grafo dirigido para modelar dependencias de habilidades.
"""
def **init**(self):
self.adyacencias = defaultdict(list) # Diccionario para almacenar las conexiones dirigidas
self.grado_entrada = defaultdict(int) # Contador de grados de entrada para cada nodo

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

if **name** == "**main**": # Crear el grafo
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

Explicación del Código

1. Clase GrafoDirigido:
   o Representa un grafo dirigido donde las aristas indican dependencias entre habilidades.
   o Usa un diccionario (adyacencias) para almacenar las conexiones dirigidas y otro (grado_entrada) para contar las dependencias de cada habilidad.
2. Métodos Principales:
   o agregar_habilidad: Añade nodos al grafo.
   o agregar_dependencia: Define una dependencia entre habilidades (arista dirigida).
   o orden_topologico: Implementa el algoritmo de Kahn para realizar el ordenamiento topológico:
    Inicia con nodos de grado de entrada 0 (sin dependencias).
    Procesa los nodos uno por uno, reduciendo el grado de entrada de sus vecinos y añadiendo nuevos nodos con grado 0 a la cola.
    Si al final todos los nodos son procesados, devuelve el orden; de lo contrario, detecta un ciclo en las dependencias.
3. Pruebas:
   o Creamos un sistema de habilidades con dependencias jerárquicas:
    "Kaioken" debe dominarse antes de "Kaioken x2", que a su vez es requisito para "Kaioken x20".
    "Super Saiyajin" habilita "Super Saiyajin 2", que es requisito para "Ultra Instinto".
   o El ordenamiento topológico devuelve el orden correcto de aprendizaje:

Orden de entrenamiento: ['Kaioken', 'Kaioken x2', 'Kaioken x20', 'Super Saiyajin', 'Super Saiyajin 2', 'Ultra Instinto'] 4. Problemas NP y Camino Mínimo (Unidad 10):
Teoría y Resolución del Problema del Camino Mínimo con Dijkstra
Teoría: Uso del Algoritmo de Dijkstra
Para resolver el problema de encontrar la mejor ruta en el universo de Dragon Ball para recolectar las Esferas del Dragón lo más rápido posible, usamos el algoritmo de Dijkstra. Este es un algoritmo eficiente que calcula el camino más corto desde un nodo inicial (planeta) a todos los demás nodos en un grafo ponderado.
En nuestro caso:
• Nodos: Representan los planetas del universo de Dragon Ball.
• Aristas: Representan las rutas espaciales entre planetas.
• Pesos: Representan el tiempo o la distancia necesaria para viajar entre planetas.
Por qué Elegimos Dijkstra

1. Eficiencia:
   o Tiene una complejidad de O((V+E)⋅log⁡V)O((V + E) \cdot \log V)O((V+E)⋅logV), donde VVV es el número de nodos y EEE el número de aristas. Esto lo hace ideal para grafos moderadamente densos como los del universo de Dragon Ball.
2. Aplicación Directa:
   o Permite calcular rutas óptimas hacia todos los planetas, lo que es esencial para recolectar las Esferas del Dragón de manera eficiente.
3. Mejora de la Jugabilidad:
   o Desde el punto de vista del jugador, este enfoque permite optimizar el tiempo de desplazamiento entre planetas, lo que mejora la fluidez y la estrategia en el juego.
   o Interfaz Clara: Proporciona una visualización de las rutas más cortas y los costos asociados, ayudando al jugador a planificar sus movimientos.
   Beneficios Adicionales
   • El uso de Dijkstra asegura que se evalúen todas las posibles rutas de manera sistemática y eficiente.
   • Su integración en el juego permite representar desafíos realistas relacionados con la logística espacial, lo que enriquece la experiencia del jugador.

CÓDIGO IMPLEMENTADO

import heapq

class Grafo:
"""
Clase que representa un grafo ponderado no dirigido para modelar el universo de Dragon Ball.
"""
def **init**(self):
self.adyacencias = {} # Diccionario para almacenar nodos y sus conexiones

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

if **name** == "**main**": # Crear el grafo
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

Explicación del Código

1. Clase Grafo:
   o Representa un grafo ponderado no dirigido, donde los nodos son planetas y las aristas tienen pesos que representan la distancia o tiempo de viaje.
2. Métodos Principales:
   o dijkstra:
    Calcula la distancia mínima desde un nodo inicial a todos los demás nodos utilizando una cola de prioridad.
    También registra los predecesores para reconstruir los caminos más cortos.
   o reconstruir_camino:
    Reconstruye la ruta más corta desde el nodo inicial hasta un nodo destino, utilizando el diccionario de predecesores generado por Dijkstra.
3. Pruebas:
   o Creamos un mapa del universo de Dragon Ball con planetas y rutas espaciales.
   o Calculamos las distancias mínimas desde "Tierra" a todos los planetas.
   o Reconstruimos y mostramos el camino más corto hacia "Planeta Freezer".

Conclusión final
Este proyecto nos permitió demostrar cómo las estructuras de datos, cuando se aplican de manera adecuada, pueden resolver problemas reales de manera eficiente y significativa.
Desde la representación del universo hasta la planificación de rutas y entrenamientos, cada decisión fue tomada para optimizar la experiencia del jugador y maximizar la funcionalidad del sistema.
El juego que decidimos crear combina estrategia, exploración y gestión de recursos en un universo inspirado en Dragon Ball Z, destacándose por su diseño técnico y las mecánicas que ofrecen una experiencia enriquecedora y estructurada para los jugadores.
El juego consiste en:
Explorar el universo:
Viajar entre diferentes planetas conectados por rutas espaciales, representados mediante un grafo ponderado, para completar misiones, recolectar recursos (como las Esferas del Dragón) y enfrentarse a desafíos.
Buscar y rescatar personajes desaparecidos:
Utilizando algoritmos como DFS y BFS para encontrar personajes y explorar áreas inexploradas, lo que aporta una mecánica de búsqueda estratégica.
Planificar entrenamientos:
Desbloquear y mejorar habilidades siguiendo dependencias jerárquicas, representadas mediante un grafo dirigido acíclico (DAG). Los jugadores progresan en su desarrollo mediante la correcta planificación de habilidades como "Kaioken" o "Super Saiyajin".
Optimizar rutas y recursos:
Resolver problemas logísticos, como encontrar las rutas más cortas para recolectar las Esferas del Dragón o viajar entre planetas, utilizando algoritmos como Dijkstra para mejorar la eficiencia en el desplazamiento.

La estructura del juego consta de los siguientes puntos:

1. Representar el Universo como un Grafo Ponderado
   Elegimos modelar los planetas y rutas del universo de Dragon Ball como un grafo ponderado no dirigido porque esta estructura refleja de forma directa la conexión entre planetas y permite incluir información relevante, como la distancia o tiempo de viaje. Esto no solo resultó lógico desde el punto de vista conceptual, sino que también permitió aplicar algoritmos como Dijkstra para calcular rutas óptimas. Esta decisión fue fundamental para mejorar la jugabilidad, ya que proporcionó al jugador herramientas estratégicas para planificar viajes de manera eficiente.
2. Implementar DFS y BFS para Exploración y Búsqueda
   La búsqueda de personajes desaparecidos y la exploración de rutas fueron resueltas mediante los algoritmos DFS y BFS. Elegimos ambos porque cada uno tiene ventajas específicas:

-  DFS es ideal para explorar caminos largos y profundos, simulando escenarios en los que el jugador necesita investigar planetas remotos.
-  BFS, en cambio, optimiza la búsqueda de caminos más cortos, adecuado para situaciones de respuesta rápida.
   Esta dualidad ofreció flexibilidad al sistema, garantizando que las búsquedas fueran completas y adaptadas a diferentes escenarios de juego.

3. Ordenamiento Topológico para Planificar Entrenamientos
   Para gestionar las habilidades de los personajes, usamos un grafo dirigido acíclico y aplicamos el ordenamiento topológico. Esta estructura fue clave para modelar las dependencias jerárquicas entre habilidades, asegurando que los personajes progresaran de manera lógica. Por ejemplo, un jugador no puede desbloquear “Kaioken x20” sin antes dominar “Kaioken x2”. Este enfoque mejoró la experiencia del usuario al ofrecer un sistema visual y estructurado, donde los jugadores podían comprender claramente qué habilidades debían desbloquearse para avanzar.
4. Resolver el Camino Mínimo con Dijkstra
   En la planificación de rutas óptimas para recolectar las Esferas del Dragón, usamos Dijkstra porque es un algoritmo eficiente para calcular caminos mínimos en grafos ponderados. Lo elegimos porque garantiza que se evalúen todas las rutas posibles de manera sistemática, optimizando la logística espacial en términos de tiempo y distancia. Esto permitió crear un sistema estratégico y fluido, donde los jugadores podían minimizar sus desplazamientos y mejorar su eficiencia en el juego.
   Interconexión de Conceptos
   Destacamos del proyecto que cada decisión estuvo fundamentada en una necesidad específica del juego. No solo seleccionamos las estructuras de datos más adecuadas, sino que también pensamos en cómo estas decisiones impactarían la jugabilidad y la experiencia del usuario. Esto nos llevó a resolver problemas que requerían tanto creatividad como rigor técnico.
   Enfoque Modular
   El diseño modular permitió que cada integrante se enfocara en un aspecto específico del sistema, ya fuera la implementación del grafo, los algoritmos de búsqueda o las jerarquías de habilidades. Esto no solo facilitó la integración del sistema, sino que también hizo posible realizar pruebas individuales de cada módulo para garantizar su correcto funcionamiento antes de combinarlos.
   Trabajo en Equipo y Aprendizaje
   La dinámica grupal nos permitió compartir conocimientos, debatir ideas y encontrar soluciones conjuntas a problemas complejos. Cada integrante aportó una perspectiva diferente, lo que enriqueció el resultado final y nos permitió avanzar con confianza en cada etapa del desarrollo.
   A nivel grupal, esta actividad fue una excelente oportunidad para aplicar el conocimiento adquirido en un contexto práctico, trabajando de manera colaborativa y enfrentando desafíos técnicos. Concluimos este proyecto con la satisfacción de haber creado un sistema robusto, escalable y alineado con los objetivos planteados, además de consolidar nuestras habilidades en programación y resolución de problemas. Estamos convencidos de que la experiencia adquirida nos preparará para afrontar proyectos más desafiantes en el futuro.
