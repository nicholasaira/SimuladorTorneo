import threading

class Simulador:
    def __init__(self):

        self._hilos = []
        self._lock = threading.Lock()