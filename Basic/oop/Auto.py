class Auto():
    color = "rojo"
    marca = "BMW"
    typo = "Electrico"
    enmarcha = False

    def arrancar(self):
        self.enmarcha = True


miCoche = Auto()
miCoche.arrancar()
print("Tipo de coche: " + miCoche.typo + " Y esta en Marcha: " + str(miCoche.enmarcha))

