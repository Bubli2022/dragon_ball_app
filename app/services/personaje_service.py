from app.models.personaje import Personaje
from config.database import db


class GestionCombates:
    @staticmethod
    def combate(personaje1, personaje2):
        """
        Ejecuta un combate entre dos personajes y devuelve al ganador.
        :param personaje1: Instancia de la clase Personaje
        :param personaje2: Instancia de la clase Personaje
        :return: Personaje ganador
        """
        print(f"{personaje1.nombre} (Poder: {personaje1.nivel_poder}) VS {personaje2.nombre} (Poder: {personaje2.nivel_poder})")
        if personaje1.nivel_poder > personaje2.nivel_poder:
            print(f"{personaje1.nombre} gana el combate.")
            return personaje1
        elif personaje2.nivel_poder > personaje1.nivel_poder:
            print(f"{personaje2.nombre} gana el combate.")
            return personaje2
        else:
            print("El combate termina en empate.")
            return None


class SubidaNivel:
    @staticmethod
    def subir_nivel(personaje_id, incremento):
        """
        Incrementa el nivel de poder de un personaje y guarda el cambio en la base de datos.
        :param personaje_id: ID del personaje en la base de datos.
        :param incremento: Valor a aumentar en el nivel de poder.
        """
        personaje = Personaje.query.get(personaje_id)
        if personaje:
            personaje.nivel_poder += incremento
            db.session.commit()
            print(f"{personaje.nombre} ha subido de nivel. Nuevo nivel de poder: {personaje.nivel_poder}")
            return personaje
        else:
            raise ValueError("Personaje no encontrado.")


class GestionHabilidades:
    @staticmethod
    def aprender_habilidad(personaje_id, habilidad):
        """
        Permite a un personaje adquirir una nueva habilidad.
        :param personaje_id: ID del personaje en la base de datos.
        :param habilidad: Nombre de la habilidad a agregar.
        """
        personaje = Personaje.query.get(personaje_id)
        if personaje:
            if habilidad not in personaje.habilidades:
                personaje.habilidades.append(habilidad)  # Asume que habilidades es una lista
                db.session.commit()
                print(f"{personaje.nombre} ha aprendido la habilidad: {habilidad}")
                return personaje
            else:
                print(f"{personaje.nombre} ya conoce la habilidad: {habilidad}")
        else:
            raise ValueError("Personaje no encontrado.")
