from herramientas.excepciones import *
from models.equipo_profesional import EquipoProfesional
from models.equipo_amateur import EquipoAmateur

class Pruebas:
    @staticmethod
    def probar_nombre_vacio():
        try:
            equipo = EquipoProfesional(1,"",1,90,80,100,nivel_entrenamiento=50)
        except nombreEquipoError as e:
            print(e)

    @staticmethod
    def probar_ranking_invalido():
        try:
            equipo = EquipoProfesional(1,"Boca fc",-7,90,80,100,nivel_entrenamiento=50)
        except rankingError as e:
            print(e)
    
    @staticmethod
    def probar_ataque_invalido():
        try:
            equipo = EquipoProfesional(1,"Boca fc",7,-6,80,100,nivel_entrenamiento=50)
        except ataqueError as e:
            print(e)

    @staticmethod
    def probar_defensa_invalida():
        try:
            equipo = EquipoProfesional(1,"Boca fc",7,60,-80,100,nivel_entrenamiento=50)
        except defensaError as e:
            print(e)

    @staticmethod
    def probar_resistencia_invalida():
        try:
            equipo = EquipoProfesional(1,"Boca fc",7,60,80,-20,nivel_entrenamiento=50)
        except resistenciaError as e:
            print(e)

    @staticmethod
    def probar_nivel_entrenamiento_invalido():
        try:
            equipo = EquipoProfesional(1,"Boca fc",7,60,80,20,nivel_entrenamiento=-50)
        except nivelEntrenamientoError as e:
            print(e)

    @staticmethod
    def probar_estado_fisico_invalido():
        try:
            equipo = EquipoAmateur(1,"Chacarita FC",40,50,50,70,estado_fisico=-10)
        except estadoFisicoError as e:
            print(e)

    @staticmethod
    def ejecutar_pruebas():
        print("\n========== PRUEBAS METODOS DE EQUIPOS ==========")
        Pruebas.probar_nombre_vacio()
        Pruebas.probar_ranking_invalido()
        Pruebas.probar_ataque_invalido()
        Pruebas.probar_defensa_invalida()
        Pruebas.probar_resistencia_invalida()
        Pruebas.probar_nivel_entrenamiento_invalido()
        Pruebas.probar_estado_fisico_invalido()

if __name__ == "__main__":
    Pruebas.ejecutar_pruebas()