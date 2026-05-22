# Lanza error cuando el ataque no esta entre 0 y 100
class ataqueError(Exception):
    def __init__(self,mensaje="El ataque debe estar entre 0 y 100"):
        super().__init__(mensaje)

# Lanza error cuando la defensa no esta entre 0 y 100
class defensaError(Exception):
    def __init__(self,mensaje="La defensa debe estar entre 0 y 100"):
        super().__init__(mensaje)


# Lanza error cuando la resistencia no esta entre 0 y 100
class resistenciaError(Exception):
    def __init__(self,mensaje="La resistencia debe estar entre 0 y 100"):
        super().__init__(mensaje)


# Lanza error cuando el ranking no esta entre 1 y 100
class rankingError(Exception):
    def __init__(self,mensaje="El ranking debe estar entre 1 y 100"):
        super().__init__(mensaje)


# Lanza error cuando el nivel de entrenamiento no esta entre 0 y 100
class nivelEntrenamientoError(Exception):
    def __init__(self,mensaje="El nivel debe estar entre 0 y 100"):
        super().__init__(mensaje)


# Lanza error cuando el estado fisico no esta entre 0 y 100
class estadoFisicoError(Exception):
    def __init__(self,mensaje="El estado fisico debe estar entre 0 y 100"):
            super().__init__(mensaje)


# Lanza error cuando se ingresa un equipo con el nombre vacio
class nombreEquipoError(Exception):
    def __init__(self,mensaje="El equipo debe tener un nombre"):
        super().__init__(mensaje)