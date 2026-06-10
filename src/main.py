import uuid

from models.torneo import Torneo
from models.equipo_profesional import EquipoProfesional
from models.equipo_amateur import EquipoAmateur
from herramientas.apiFootball import ApiFootball
from logica.simulador import Simulador


API_KEY = "59ae5be1a5111dbdfd842ec8e6e2c473"


def main():

    api = ApiFootball(API_KEY)

    #Recojo los datos de la liga argentina temporada 2022
    datos = api.obtener_datos_equipos(
        liga=128,
        temporada=2022
    )
    #Creo torneo
    torneo = Torneo(
        uuid.uuid4(),
        "Liga Simulada"
    )

    equipos = []
    #Recorre los equipos 
    for i, dato in enumerate(datos):
        #Crea mitad profesionales, mitad amateurs
        if i % 2 == 0:
            equipo = EquipoProfesional(dato["id"],dato["nombre"],dato["ranking"],dato["ataque"],dato["defensa"],dato["resistencia"],85)
        else:
            equipo = EquipoAmateur(dato["id"],dato["nombre"],dato["ranking"],dato["ataque"],dato["defensa"],dato["resistencia"],75)

        equipos.append(equipo)
        torneo.agregar_equipo(equipo)

    print(f"Equipos cargados: {len(equipos)}")

    # Si la cantidad es impar, sacar uno
    if len(torneo.get_equipos) % 2 != 0:
        eliminado = torneo.get_equipos.pop()
        print(f"Se eliminó {eliminado.get_nombre()} "
             f"para tener cantidad par de equipos.")
    #Genera las fechas el torneo
    torneo.generar_fechas()
    #Inicia el simulador
    simulador = Simulador()

    #Recorre las fechas y las juega
    for numero_fecha, fecha in enumerate(torneo.get_fechas,start=1):
        print(f"\n========== FECHA {numero_fecha} ==========")
        #Limpia las fechas anteriores
        simulador.limpiar()
        #Simula la fecha
        simulador.ejecutar_fecha(fecha)
        #Muestra los resultados de la fecha
        simulador.mostrar_resultados()
        #Muestra la tabla de puntos 
        torneo.mostrar_tabla()

    print("\n========== CAMPEÓN ==========")
    print(torneo.obtener_campeon())

    torneo.guardar_tabla_csv("src/datos/tabla_final.csv")
    print("Tabla final guardada correctamente")

if __name__ == "__main__":
    main()