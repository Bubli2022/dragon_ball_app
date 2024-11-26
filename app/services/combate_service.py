from app.models.combate import Combate
from app.models.personaje import Personaje
from config.database import db

class CombateService:
    @staticmethod
    def ejecutar_combate(personaje1_id, personaje2_id):
        """
        Ejecuta un combate entre dos personajes y registra el resultado.
        :param personaje1_id: ID del primer personaje
        :param personaje2_id: ID del segundo personaje
        :return: Registro del combate
        """
        personaje1 = Personaje.query.get(personaje1_id)
        personaje2 = Personaje.query.get(personaje2_id)

        if not personaje1 or not personaje2:
            raise ValueError("Uno o ambos personajes no existen.")

        # Determinar ganador
        if personaje1.nivel_poder > personaje2.nivel_poder:
            ganador = personaje1
            resultado = f"Ganador: {personaje1.nombre}"
        elif personaje2.nivel_poder > personaje1.nivel_poder:
            ganador = personaje2
            resultado = f"Ganador: {personaje2.nombre}"
        else:
            ganador = None
            resultado = "Empate"

        # Registrar el combate en la base de datos
        combate = Combate(
            personaje1_id=personaje1_id,
            personaje2_id=personaje2_id,
            ganador_id=ganador.id if ganador else None,
            resultado=resultado
        )
        db.session.add(combate)
        db.session.commit()

        return combate
