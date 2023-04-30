class DispositivoEntrada:
    tipoEntrada = str
    marca = str

    def __init__(self,tipoEntrada,marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca
    
    @property
    def tipoEntrada(self):
        return self._tipoEntrada
    @tipoEntrada.setter
    def tipoEntrada(self,tipoEntrada):
        self._tipoEntrada = tipoEntrada
    
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    
    def __str__(self):
        return f'DispositivoEntrada: [TipoEntrada: {self.tipoEntrada}, Marca: {self.marca}]'

if __name__ == "__main__":
    test = DispositivoEntrada("Usb","Msi")
    print(test)
    


