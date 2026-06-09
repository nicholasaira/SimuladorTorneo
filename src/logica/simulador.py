import threading
import time

class Simulador:
    def __init__(self):
        self._threads = []
        self._resultados = []
        self._lock = threading.Lock()

    #Metodo que retorna el threads
    def get_threads(self):
        return self._threads

    #Metodo que retorna los resultados
    def get_resultados(self):
        return self._resultados
    
    #Limpia los resultados del simulador
    def limpiar(self):
        self._threads.clear()
        self._resultados.clear()
    
    #Metodo que realiza la simulacion del partido
    def simular_partido(self, partido):

        print(
            f"[{threading.current_thread().name}] "
            f"Simulando {partido}"
        )

        time.sleep(2)

        partido.jugar_partido()

        with self._lock:
            self._resultados.append(partido)

        print(
            f"[{threading.current_thread().name}] "
            f"Finalizado {partido}"
        )

    def ejecutar_fecha(self, fecha):

        self._threads = []

        for partido in fecha:

            thread = threading.Thread(
                target=self.simular_partido,
                args=(partido,)
            )

            self._threads.append(thread)
            thread.start()

        for thread in self._threads:
            thread.join()

    def mostrar_resultados(self):
        print("\n========== RESULTADOS ==========")
        for partido in self._resultados:
            partido.mostrar_resultado()

    def __str__(self):
        return f"Simulador con {len(self._threads)} hilos"