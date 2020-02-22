class Auto():
    color = "rojo"
    marca = "BMW"
    typo = "Electrico"
    enmarcha = False

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if self.enmarcha:
            return "El coche esta en marcha"
        else:
            return "El Coche esta parado"


miCoche = Auto()
miCoche.arrancar()
print("Tipo de coche: " + miCoche.typo + " Y esta en Marcha: " + str(miCoche.enmarcha))

print(miCoche.estado())

