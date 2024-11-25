from flask import Flask
from config.database import init_app
from app.routes.personajes import personajes_bp
from app.routes.habilidades import habilidades_bp

def create_app():
    app = Flask(__name__)
    init_app(app)
    app.register_blueprint(personajes_bp, url_prefix='/api/personajes')
    app.register_blueprint(habilidades_bp, url_prefix='/api/habilidades')
    return app
