class Persona():
    def __init__(self, nombre, edad, lugarResidencia):

        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia  = lugarResidencia

    def descripcion(self):
        print(f"Nombre {self.nombre} , edad: {self.edad} y Lugar de resedencia: {self.lugarResidencia}")

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, residencia):
        super().__init__(nombre , edad , residencia)
        self.salario = salario
        self.antiguedad = antiguedad


    def descripcion(self):
        super().descripcion()
        print(f"Salario{self.salario} y Antiguedad: {self.antiguedad}")


harry = Persona("Harry", 23, "Tura")

harry.descripcion()

ender = Empleado(10000, 23, "ander", 32, "Medellin")

ender.descripcion()

print(isinstance(harry, Empleado))