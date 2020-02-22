class Auto():

    def __init__(self):
        self.__color = "rojo"
        self.__marca = "BMW"
        self.__typo = "Electrico"
        self.__enmarcha = False

    def arrancar(self, arrancar):

        self.__enmarcha = arrancar
        if self.__enmarcha:
            chequeo = self.__chequeoInterno()

        if self.__enmarcha and chequeo:
             return "El coche esta en marcha"
        elif self.__enmarcha and chequeo == False:
            return "Algo a paso en el chequeo"
        else:
             return "El Coche esta parado"


    def estado(self):
       print(f" El choche es marca {self.__marca} y color {self.__color}")
           

    def __chequeoInterno(self):
        print("Realizado chequeo interno")
        self.gasolina = "ok"
        self.aceite= "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else : 
            return False


miCoche = Auto()
print(miCoche.arrancar(True))
# print("Tipo de coche: " + miCoche.typo + " Y esta en Marcha: " + str(miCoche.enmarcha))

miCoche.estado()

