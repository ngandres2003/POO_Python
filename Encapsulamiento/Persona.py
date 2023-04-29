class Persona:
    #Atributos de una clase
    def __init__(self, nombre,apellido,edad):#Metodo constructor
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    #Metodo de una clase
    def mostrar_detalle(self):
        print(f" Persona: {self._nombre}, Apellido: {self.apellido}, Edad: {self.edad}")

    ''' @Propertyse utiliza para convertir un método de una clase en un atributo de solo lectura. 
    Esto significa que el método se comporta como si fuera un atributo, permitiendo que se acceda
    a él sin la necesidad de invocar el método explícitamente.'''
    
    
    @property 
    def nombre(self):
        print("si se uso")
        return self._nombre
    '''El decorador @setter se utiliza en conjunción con el decorador @property para crear un método que permite 
    establecer el valor de un atributo protegido de una clase desde el exterior de la misma.'''

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
        print("se uso")
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        self._edad = edad
    
    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido}")


if __name__ =="__main__": 
    persona1 = Persona("Andres","Ng",19)
    persona1.edad = 6
    print(persona1.edad)


    

