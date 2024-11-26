from app import create_app
from app.services.torneo_service import Torneo
from app.routes.torneos import torneos_bp
from config.database import init_app  
from app.routes.personajes import personajes_bp
from app.services.arbol_service import ArbolBinarioDeBusqueda
from app.services.arbol_habilidades_service import ArbolHabilidades
from app.services.grafo_service import Grafo
from app.routes.grafo import grafo_bp
from app.services.habilidades_service import GrafoDirigido
from app.routes.habilidades_grafo import habilidades_grafo_bp
from app.routes.combate import combates_bp

app = create_app()


# Inicializa la configuración de la base de datos y migraciones
init_app(app)

# Instancia global del torneo
torneo_global = Torneo()

# Crear una instancia global de los árboles de habilidades y personajes
arbol_personajes = ArbolBinarioDeBusqueda()
arbol_habilidades = ArbolHabilidades("Kamehameha")

# Instancia global del grafo
universo_grafo = Grafo()

# Instancia global del grafo de habilidades
grafo_habilidades = GrafoDirigido()

# Registro de las rutas
app.register_blueprint(personajes_bp, url_prefix='/api/personajes')

app.register_blueprint(torneos_bp, url_prefix='/api/torneos')

app.register_blueprint(grafo_bp, url_prefix='/api/grafo')

app.register_blueprint(habilidades_grafo_bp, url_prefix='/api/habilidades_grafo')

app.register_blueprint(grafo_bp, url_prefix='/api/grafo')

app.register_blueprint(combates_bp, url_prefix='/api/combates')

if __name__ == '__main__':
    app.run(debug=True)
