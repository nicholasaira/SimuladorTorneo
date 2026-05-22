from models.equipo import Equipo
from models.partido import Partido

class Torneo:
    def __init__(self, id_torneo, nombre):
        self._id = id_torneo
        self._nombre = nombre
        self._equipos = []
        self._partidos = []
        self._campeon = None
        self._fecha_inicio = None
        self._fecha_fin = None