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

    #Calcula la potencia en base a sus atributos y un factor suerte que afecta entre 20% por arriba o por abajo de su potencia
    def calcular_potencia(self):

        potencia_base = (
            self._ataque * 0.25 +
            self._defensa * 0.20 +
            self._resistencia * 0.20 +
            self._estado_fisico * 0.35
        )

        factor = random.uniform(0.8, 1.2)

        return potencia_base * factor
    
    #Aumenta el estado fisico en 10, el estado maximo es 100
    def recuperar_fisico(self):
        self._estado_fisico += 10
        if (self._estado_fisico>100):
            self._estado_fisico=100