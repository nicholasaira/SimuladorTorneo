from models.equipo import Equipo

class EquipoProfesional(Equipo):

    def __init__(
        self,
        id_equipo,
        nombre,
        ranking,
        ataque,
        defensa,
        resistencia,
        patrocinador,
        nivel_entrenamiento
    ):

        super().__init__(
            id_equipo,
            nombre,
            ranking,
            ataque,
            defensa,
            resistencia
        )

        self._patrocinador = patrocinador
        self._nivel_entrenamiento = nivel_entrenamiento