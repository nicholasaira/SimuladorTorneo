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

    #Metodo privado que valida las entradas para lanzar la excepcion
    def _validar_rango(self,valor, minimo, maximo, excepcion):
        if (valor < minimo or valor > maximo):
            raise excepcion
    #Metodo privado que valida el nombre del equipo
    def _validar_nombre(self,nombre,excepcion):
        if nombre.strip() == "":
            raise excepcion

    #Metodo que se encarga de calcular la potencia de un equipo
    @abstractmethod
    def calcular_potencia(self):
        pass

    #Metodo para setear el ataque
    def setAtaque(self,ataque):
        self._validar_rango(ataque,0,100,ataqueError())
        self._ataque = ataque

    #Metodo para setear la defensa
    def setDefensa(self,defensa):
        self._validar_rango(defensa,0,100,defensaError())
        self._defensa = defensa

    #Metodo para setear la resistencia
    def setResistencia(self, resistencia):
        self._validar_resistencia(resistencia,0,100,resistenciaError())
        self._resistencia = resistencia

    #Metodo para aumentar las victorias del equipo
    def guardar_victoria(self):
        self._victorias+=1

    #Metodo que muestra los stats del equipo
    def mostrar_estadisticas(self):
        print("Equipo: ",self._nombre)
        print("Victorias: ",self._victorias)
        print("Empates: ",self._empates)
        print("Derrotas: ",self._derrotas)
        print("Goles a favor: ",self._goles_favor)
        print("Goles en contra: ",self._goles_contra)
    
    def __str__(self):
        return (self._nombre, " | ", self._ranking)