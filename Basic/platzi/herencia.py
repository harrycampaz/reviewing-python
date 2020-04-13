class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def miNombre(self):
        print(f"Nombre de la figura : {self.nombre} ")

class Rectangulo(Figura):
    def __init__(self, base, altura, nombre):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def miNombre(self):
        print("Rectangulo ")

class Cuadrado(Rectangulo):

    def __init__(self, lado, nombre):
        super().__init__(lado, lado, nombre)

    def miNombre(self):
        print("Cuadrado ")




def main():

    rectangulo = Rectangulo(base = 3, altura= 4, nombre= "rectangulo")

    print(rectangulo.area())

    rectangulo.miNombre()

    cuadrado = Cuadrado(lado= 5, nombre= "cuadrado")

    print(cuadrado.area())

    cuadrado.miNombre()

if __name__ == "__main__":
      
  main()