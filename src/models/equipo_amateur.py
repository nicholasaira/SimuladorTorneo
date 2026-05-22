import random
from models.equipo import Equipo
from herramientas.excepciones import (estadoFisicoError)


class EquipoAmateur(Equipo):
    def __init__(
        self,
        id_equipo,
        nombre,
        ranking,
        ataque,
        defensa,
        resistencia,
        estado_fisico:int
    ):

        super().__init__(
            id_equipo,
            nombre,
            ranking,
            ataque,
            defensa,
            resistencia
        )

        self._validar_rango(estado_fisico,0,100,estadoFisicoError())
        self._estado_fisico = estado_fisico

    #Calcula la potencia en base a sus atributos y un factor suerte entre 1 y 15
    def calcular_potencia(self):
        potencia = (self._ataque+self._defensa+self._resistencia+self._estado_fisico+(100-self._ranking)+random.randint(1,15))
        return potencia
    
    #Aumenta el estado fisico en 10, el estado maximo es 100
    def recuperar_fisico(self):
        self._estado_fisico += 10
        if (self._estado_fisico>100):
            self._estado_fisico=100