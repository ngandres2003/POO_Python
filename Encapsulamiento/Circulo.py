import math
class Circulo:
    def __init__(self,radio):
        self.radio = radio
        self._pi = math.pi

    def calcular_area(self):
        return self._pi * self.radio**2
    
    @property
    def pi(self):
        return self._pi

circulo_1 = Circulo(5)
print(circulo_1.pi)

