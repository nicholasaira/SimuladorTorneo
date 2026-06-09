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

    #Calcula la potencia en base a sus atributos y un factor suerte entre un 10% que afecta por encima o por debajo de su potencia
    def calcular_potencia(self):

        potencia_base = (
            self._ataque * 0.30 +
            self._defensa * 0.25 +
            self._resistencia * 0.20 +
            self._nivel_entrenamiento * 0.25
        )

        factor = random.uniform(0.9, 1.1)

        return potencia_base * factor
    
    #Metodo para aumentar ataque,defensa y nivel de entrenamiento (el maximo es 100)
    def entrenar(self):
        self._ataque += 2
        self._defensa += 1
        self._nivel_entrenamiento += 1
        if (self._nivel_entrenamiento > 100):
            self._nivel_entrenamiento = 100