from app.models.planeta import Planeta
from config.database import db

class PlanetaService:
    @staticmethod
    def agregar_planeta(nombre, descripcion=None, distancia_tierra=None):
        """
        Agrega un nuevo planeta a la base de datos.
        :param nombre: Nombre del planeta.
        :param descripcion: Descripción del planeta.
        :param distancia_tierra: Distancia del planeta a la Tierra.
        """
        if Planeta.query.filter_by(nombre=nombre).first():
            raise ValueError(f"El planeta '{nombre}' ya existe.")

        nuevo_planeta = Planeta(
            nombre=nombre,
            descripcion=descripcion,
            distancia_tierra=distancia_tierra
        )
        db.session.add(nuevo_planeta)
        db.session.commit()
        return nuevo_planeta

    @staticmethod
    def listar_planetas():
        """
        Obtiene todos los planetas de la base de datos.
        """
        return Planeta.query.all()

    @staticmethod
    def buscar_planeta(nombre):
        """
        Busca un planeta por nombre.
        :param nombre: Nombre del planeta.
        """
        return Planeta.query.filter_by(nombre=nombre).first()

    @staticmethod
    def eliminar_planeta(nombre):
        """
        Elimina un planeta de la base de datos.
        :param nombre: Nombre del planeta.
        """
        planeta = Planeta.query.filter_by(nombre=nombre).first()
        if not planeta:
            raise ValueError(f"El planeta '{nombre}' no existe.")
        
        db.session.delete(planeta)
        db.session.commit()
        return f"Planeta '{nombre}' eliminado con éxito."
