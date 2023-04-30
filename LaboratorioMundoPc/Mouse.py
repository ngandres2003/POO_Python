from DispositivosEntrada import DispositivoEntrada

class Mouse(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Mouse.contadorRatones += 1
        self._idmouse = Mouse.contadorRatones
    
    @property
    def idMouse(self):
        return self._idmouse
    @idMouse.setter
    def idMouse(self,idMouse):
        self._idmouse = idMouse
    
    def __str__(self):
        return f"Mouse: [IdMouse: {self.idMouse}], {super().__str__()} "

if __name__ == "__main__":
    test = Mouse("Usb","Msi")
    test_2 = Mouse("Usb","Asus")
    print(test)
    print(test_2)