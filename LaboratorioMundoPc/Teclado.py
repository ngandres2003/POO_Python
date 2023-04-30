from DispositivosEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclado = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Teclado.contadorTeclado += 1
        self._idTeclado = Teclado.contadorTeclado
    
    @property
    def idTeclado(self):
        return self._idTeclado
    @idTeclado.setter
    def idTeclado(self,idTeclado):
        self._idTeclado = idTeclado
    
    def __str__(self):
        return f'Teclado: [IdTeclado: {self.idTeclado}], {super().__str__()}'

if __name__ == "__main__":
    test = Teclado("Usb C","Apple")
    print(test)