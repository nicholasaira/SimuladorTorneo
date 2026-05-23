from models.partido import Partido
from herramientas.excepciones import cantidadEquiposError
import uuid
#
class Torneo:
    def __init__(self, id_torneo, nombre):
        self._id = id_torneo
        self._nombre = nombre
        self._equipos = []
        self._partidos = []
        self._campeon = None

    def get_nombre(self):
        return self._nombre

    def get_equipos(self):
        return self._equipos

    def get_partidos(self):
        return self._partidos

    def agregar_equipo(self, equipo):
        self._equipos.append(equipo)

    def generar_partidos(self):
        if len(self._equipos) < 2:
            raise cantidadEquiposError()

        if len(self._equipos) % 2 != 0:
            raise cantidadEquiposError()

        for i in range(0, len(self._equipos), 2):
            partido = Partido(
                uuid.uuid4(),
                self._equipos[i],
                self._equipos[i + 1]
            )
            self._partidos.append(partido)

    def iniciar_torneo(self):
        print("\nTorneo:", self._nombre)
        for partido in self._partidos:
            partido.jugar_partido()
            partido.mostrar_resultado()

    def mostrar_tabla(self):
        print("\nTabla de posiciones:")
        for equipo in self._equipos:
            equipo.mostrar_estadisticas()

    def obtener_campeon(self):
        for equipo in self._equipos:
            puntos = equipo.get_victorias() * 3 + equipo.get_empates()
            equipo.set_puntos_totales(puntos)

        return max(self._equipos, key=lambda e: e.get_puntos_totales())

    def __str__(self):
        return f"Torneo: {self._nombre}"