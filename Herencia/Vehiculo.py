class Vehiculo:
    def __init__(self,color,precio):
        self._color = color
        self._precio = precio
    def __str__(self):
        return f"Vehiculo[Color:{self._color}, Precio:{self._precio}]"
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color
    
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,precio):
        self._precio = precio


class Carro(Vehiculo):
    def __init__(self, color,precio,modelo,placa):
        super().__init__(color, precio)
        self.modelo = modelo
        self.placa = placa
    def __str__(self):
        return f'{super().__str__()} Modelo:{self.modelo}, Placa:{self.placa}'


class Bicicleta(Vehiculo):
    def __init__(self, color, precio,tipo):
        super().__init__(color, precio)
        self.tipo = tipo
    def __str__(self):
        return f'{super().__str__()} Tipo: {self.tipo}'
    
