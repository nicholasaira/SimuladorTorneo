from abc import ABC, abstractmethod
from herramientas.excepciones import (ataqueError,defensaError,resistenciaError,rankingError,nombreEquipoError)

class Equipo(ABC):
    def __init__(self, id_equipo:str, nombre:str, ranking:int, ataque:int, defensa:int, resistencia:int):
        self._validar_nombre(nombre,nombreEquipoError())
        self._validar_rango(ataque,0,100,ataqueError())
        self._validar_rango(defensa,0,100,defensaError())
        self._validar_rango(ranking,1,100,rankingError())
        self._validar_rango(resistencia,0,100,resistenciaError())
        self._id = id_equipo
        self._nombre = nombre
        self._ranking = ranking
        self._ataque = ataque
        self._defensa = defensa
        self._resistencia = resistencia
        self._victorias = 0
        self._empates = 0
        self._derrotas = 0
        self._goles_favor = 0
        self._goles_contra = 0
        self._puntos_totales = 0
