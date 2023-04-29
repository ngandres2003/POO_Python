from abc import ABC,abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
        if ancho > 0:
            self._ancho = ancho
        else:
            self._ancho = 0
        if alto > 0:
            self._alto = alto
        else:
            self._alto = 0

    def __str__(self):
        return f"alto: {self._alto}, ancho: {self._ancho}"
    
    @property
    def get_ancho(self):
        return self._ancho
    
    @property
    def get_alto(self):
        return self._alto
  
    #Abstraccion evita instanciar la clase padre y obligar a las clases hijas agregar el metodo seleccionado
    @abstractmethod
    def calcular_area(self):
        pass