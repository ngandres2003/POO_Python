class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __add__(self,other):
        return self.nombre + other.nombre
    
    def __sub__(self,other):
        return self.edad - other.edad
    

objeto1 = Persona("Andres",20)
object2 = Persona("Jesus",12)

print(objeto1 + object2)
print(objeto1 - object2)