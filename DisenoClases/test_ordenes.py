from Orden import Orden
from Producto import Producto


Producto1 = Producto("Camisa",100.00)
producto2 = Producto("Pantalon",500.00)
prducto3 = Producto("Calcetin",50.00)
producto4 = Producto("Blusa",70.00)

productos = [Producto1,producto2]
productos2 = [prducto3,producto4]


orden1 = Orden(productos)
orden1.agregar_producto(prducto3)
print(orden1)
print(orden1.calcular_total())
orden2 = Orden(productos2)
orden2.agregar_producto(Producto1)
print(orden2)
print(orden2.calcular_total())

        
        
