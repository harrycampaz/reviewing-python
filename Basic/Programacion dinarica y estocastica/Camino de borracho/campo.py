class Campo:

    def __init__(self):
        self.coodenadas_borracho = {}

    def anadir_borracho(self, borracho, coordenadas):
        self.coodenadas_borracho[borracho] = coordenadas

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenadas_actual = self.coodenadas_borracho[borracho]
        nueva_coordenada = coordenadas_actual.mover(delta_x, delta_y)

        self.coodenadas_borracho[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coodenadas_borracho[borracho]
