class Persona:
    #Atributos de una clase
    def __init__(self, nombre,apellido,edad):#Metodo constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    #Metodo de una clase
    def mostrar_detalle(self):
        print(f" Persona: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}")

persona1 = Persona("Andres","Ng","20") #Creamos una instancia de la clase Persona
persona1.mostrar_detalle() #Accedemos al metodo de la clase

persona2 = Persona("Jennire","Vetri","19")#Creamos una instancia de la clase Persona
print(vars(persona2)) #Imprimimos los atributos de los objetos en un formato dict()

persona3 = Persona("Lolo","Perez","11")#Creamos una instancia de la clase Persona
Persona.mostrar_detalle(persona3) #Accedemos al metodo directamente pasandole como self el objeto creado

persona1.telefono = 354636 #Agregamos un atributo solamente al obejeto de persona1, este atributo no se comparte ni se agrega a la clase
print(persona1.telefono)

