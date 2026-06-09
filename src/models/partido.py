import random

class Partido:

    def __init__(self, id_partido, local, visitante):

        self._id = id_partido
        self._local = local
        self._visitante = visitante

        self._goles_local = 0
        self._goles_visitante = 0

    #Metodo que se encarga de la simulacion de un partido 
    def jugar_partido(self):

        #Calcula la potencia de cada equipo
        potencia_local = self._local.calcular_potencia()
        potencia_visitante = self._visitante.calcular_potencia()

        # Ventaja al equipo local del 5%
        potencia_local *= 1.05

        diferencia = potencia_local - potencia_visitante

        #El partido comienzan ambos entre 0 y 2 goles
        self._goles_local = random.randint(0, 2)
        self._goles_visitante = random.randint(0, 2)

        #Genera los goles en base a la diferencia de potencias
        if diferencia > 15:
            self._goles_local += random.randint(1, 3)

        elif diferencia > 5:
            self._goles_local += random.randint(0, 2)

        elif diferencia < -15:
            self._goles_visitante += random.randint(1, 3)

        elif diferencia < -5:
            self._goles_visitante += random.randint(0, 2)

        #Actualizar goles a favor del local
        self._local.agregar_goles_favor(self._goles_local)
        #Actualiza goles en contra del visitante
        self._local.agregar_goles_contra(self._goles_visitante)
        #Actualiza goles a favor del visitante
        self._visitante.agregar_goles_favor(self._goles_visitante)
        #Actualiza goles en contra del local
        self._visitante.agregar_goles_contra(self._goles_local)

        # Determina el resultado en base a los goles de cada equipo
        if self._goles_local > self._goles_visitante:
            self._local.guardar_victoria()
            self._visitante.guardar_derrota()

        elif self._goles_local < self._goles_visitante:
            self._visitante.guardar_victoria()
            self._local.guardar_derrota()

        else:
            self._local.guardar_empate()
            self._visitante.guardar_empate()

    def mostrar_resultado(self):
        print(
            f"{self._local.get_nombre()} "
            f"{self._goles_local} - "
            f"{self._goles_visitante} "
            f"{self._visitante.get_nombre()}"
        )

    def __str__(self):
        return (
            f"{self._local.get_nombre()} "
            f"vs "
            f"{self._visitante.get_nombre()}"
        )