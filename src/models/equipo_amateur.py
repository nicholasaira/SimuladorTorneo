from models.equipo import Equipo

class EquipoAmateur(Equipo):
    def __init__(
        self,
        id_equipo,
        nombre,
        ranking,
        ataque,
        defensa,
        resistencia,
        club,
        division,
        estado_fisico
    ):

        super().__init__(
            id_equipo,
            nombre,
            ranking,
            ataque,
            defensa,
            resistencia
        )

        self._club = club
        self._division = division
        self._estado_fisico = estado_fisico