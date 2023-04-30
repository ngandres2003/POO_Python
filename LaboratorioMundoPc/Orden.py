from Monitor import Monitor
from Teclado import Teclado
from Mouse import Mouse
from Computadora import Computadora

class Orden:
    contadorOrdenes = 0

    def __init__(self,computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = computadoras
    
    def agregar_pc(self,computadora):
        self._computadoras.append(computadora)
    
    def __str__(self):
        computadoras_str = ""
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f"""
            Orden: {self._idOrden}
            Computadora: {computadoras_str}
        
        """

monitor = Monitor("Msi","24")
teclado = Teclado("usb","logitech")
mouse = Mouse("usb","asus")
computadora = Computadora("Tuf dash",monitor,teclado,mouse)

monitor2 = Monitor("razer","24")
teclado2 = Teclado("usb","Apple")
mouse2 = Mouse("usb","razer")
computadora2 = Computadora("macm1",monitor,teclado,mouse)

computadoras = [computadora, computadora2]
orden = Orden(computadoras)
print(orden)
    
    
    
    