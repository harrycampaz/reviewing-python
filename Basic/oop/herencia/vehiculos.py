class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.accelerar = False
        self.frenar = False
        
    def arrancar(self):
        self.enmarcha = True

    def acceledado(self):
        self.accelerar = True
    
    def frenado(self):
        self.frenar = True

    def estado(self):
        print(f"Marca: {self.marca} \nmodelo: {self.modelo} \nAcelerando: {self.accelerar} \nFrenar: {self.frenar} ")

class Furgoneta(Vehiculo):
    def carga(self, carga):
        self.cargado = carga

        if self.cargado:
            return "La furgoneta esta cargada"
        else: 
            return "La furgoneta no esta cargada"

class VElectrico():

    def __init__(self):
        self.autonomia = 100
    def cargarEnergia(self):
        self.cargado = True



class Moto(Vehiculo):
    caballito = ""

    def doCaballito(self):
        self.caballito = "Voy en una rueda"
    
    def estado(self):
        print(f"Marca: {self.marca} \nmodelo: {self.modelo} \nAcelerando: {self.accelerar} \nFrenar: {self.frenar} \n{self.caballito}")



# miMoto = Moto("Yamaha", "BWS")
# miMoto.doCaballito()
# miMoto.estado()

miFutgo = Furgoneta("Volvo", "drinn")
miFutgo.estado()
print(miFutgo.carga(False))



class BicicletaElectrica(Vehiculo, VElectrico):
    pass

#Herencias Multiples
#Toma el constructor de la primera clase en la herencia multiple
miBici = BicicletaElectrica("Hawa", "Cons")