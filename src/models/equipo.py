from abc import ABC, abstractmethod

class Equipo(ABC):
    def __init__(self, id_equipo, nombre, ranking, ataque, defensa, resistencia):
        self._id = id_equipo
        self._nombre = nombre
        self._ranking = ranking
        self._ataque = ataque
        self._defensa = defensa
        self._resistencia = resistencia
        self._victorias = 0