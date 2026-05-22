from logica.simulador import Simulador
import time

def prueba_simulador():
    simulador = Simulador()

    #Modifico el sleep para que no demore 2 segundos por cada hilo en la prueba
    sleep_original = time.sleep
    time.sleep = lambda x: None

    try:
        class PartidoInventado:
            def __init__(self):
                self.jugado = False

            def jugar_partido(self):
                self.jugado = True

        partidos = [PartidoInventado() for _ in range(5)]

        simulador.ejecutar_simulaciones(partidos)

        assert len(simulador.get_resultados()) == 5     #Verifica que la lista de resultados guardó 5 partidos
        assert all(p.jugado for p in partidos)          #Verifica que todos los partidos hayan sido ejecutados (jugado = True)
        assert simulador.get_resultados() == partidos   #Verifica que se hayan guardado los mismos objetos en el mismo orden

    #Dejo todo como antes
    finally:
        time.sleep = sleep_original

if __name__ == "__main__":
    prueba_simulador()
    print("TODOS LOS TESTS OK")