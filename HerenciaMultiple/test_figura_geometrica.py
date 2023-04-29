from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica
cuadrado1 = Cuadrado(5,"rojo")
print(cuadrado1.calcular_area())
print(cuadrado1)

rectangulo1 = Rectangulo(4,20,"Verde")
print(rectangulo1.calcular_area())
print(rectangulo1)

# #No se puede instanciar una clase abstracta
# figura = (FiguraGeometrica(12,13))