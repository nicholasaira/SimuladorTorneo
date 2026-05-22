from models.equipo import Equipo
from datetime import datetime

class Partido:

    def __init__(self, id_partido, equipo_local, equipo_visitante):

        self._id = id_partido
        self._equipo_local = equipo_local
        self._equipo_visitante = equipo_visitante

        self._resultado = ""
        self._ganador = None
        self._fecha = datetime.now()  