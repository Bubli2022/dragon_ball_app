from flask import Flask
from config.database import init_app
from app.routes.personajes import personajes_bp

app = Flask(__name__)
init_app(app)

# Registro de rutas
app.register_blueprint(personajes_bp)

if __name__ == '__main__':
    app.run(debug=True)
