import random
from models.equipo import Equipo
from herramientas.excepciones import (nivelEntrenamientoError)

class EquipoProfesional(Equipo):

    def __init__(
        self,
        id_equipo,
        nombre,
        ranking,
        ataque,
        defensa,
        resistencia,
        nivel_entrenamiento:int
    ):

        super().__init__(
            id_equipo,
            nombre,
            ranking,
            ataque,
            defensa,
            resistencia
        )

        self._validar_rango(nivel_entrenamiento,0,100,nivelEntrenamientoError())
        self._nivel_entrenamiento = nivel_entrenamiento

    #Calcula la potencia en base a sus atributos y un factor suerte entre 1 y 20
    def calcular_potencia(self):
        potencia = (self._ataque+self._defensa+self._resistencia+self._nivel_entrenamiento+(100-self._ranking)+random.randint(1,20))
        return potencia
    
    #Metodo para aumentar ataque,defensa y nivel de entrenamiento (el maximo es 100)
    def entrenar(self):
        self._ataque += 2
        self._defensa += 1
        self._nivel_entrenamiento += 1
        if (self._nivel_entrenamiento > 100):
            self._nivel_entrenamiento = 100