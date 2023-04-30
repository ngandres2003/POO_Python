from Monitor import Monitor
from Teclado import Teclado
from Mouse import Mouse

class Computadora:
    contadorComputadoras = 0

    def __init__(self,nombre,monitor,teclado,mouse):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    def __str__(self):
        return f"Computadora: [IdComputadora: {self._idComputadora}, Nombre: {self._nombre}, {self._monitor}, {self._teclado}, {self._mouse}]"

if __name__ == "__main__":
    monitor = Monitor("Msi","24")
    teclado = Teclado("usb","logitech")
    mouse = Mouse("usb","asus")
    computadora = Computadora("Tuf dash",monitor,teclado,mouse)
    print(computadora)