class MiClase:

    variable_clase = "Variable clase"

    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia

    #Metodo Estatico, es instrinsico de la clase y no puede acceder a los objetos creados o de instancia (self)
    @staticmethod
    def metodo_estatico():
        #Podemos acceder a las variables de clase llamando a la clase -> Miclase.variable_clase
        return "Estas usando un metodo estatico"
    
    #Metodo de clase
    @classmethod
    def metodo_clase(cls):
        return cls.variable_clase

print(MiClase.variable_clase)

clase = MiClase("Variable de instancia")
print(clase.variable_instancia)
print(clase.variable_clase)

#Agregamos una variable de clase
MiClase.variable_clase2 = "Variable de clase 2"
print(MiClase.variable_clase2)

#Imprimimos el metodo estatico 
print(MiClase.metodo_estatico())

#Imprimimos el metodo de clase
print(MiClase.metodo_clase())

#Imprimimos el metodo de clase desde un objeto 
objeto1 = MiClase("Variable instancia")
print(objeto1.metodo_clase())