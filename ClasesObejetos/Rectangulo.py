class Rectangulo:

    def __init__(self,base,height):#Atributos de la clase
        self.base = base
        self.height = height

    def calcular_area(self):#Metodos de la clase
        return self.base * self.height
    
rectangulo_1 = Rectangulo(5,2)
print("El area del rectangulo es:",rectangulo_1.calcular_area())

