from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    
    if isinstance(objeto,Gerente):
        print(objeto.departamento)

empleado = Empleado("Juan", 5000)
imprimir_detalles(empleado)


gerente = Gerente("Andres", 10000,"Sistemas")
imprimir_detalles(gerente)