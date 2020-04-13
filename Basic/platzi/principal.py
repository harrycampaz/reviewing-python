class Carro():
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._data1 = None

    @property
    def modelo(self):
        return self._modelo
    
    @data1.setter
    def set_data1(self, data1):
        if data1 in self._modelo:
            self._data1 = data1
        raise ValueError(f'el modelo {data1} no es valido para la marcas {self._marca}')

    @property
    def marca(self):
        return self._marca


carro = Carro("Mazda", ["3", "2" , "5"])

# print(carro.modelo)
#print(carro.marca)

carro.data = "9"