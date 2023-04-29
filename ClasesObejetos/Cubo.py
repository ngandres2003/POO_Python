class Cubo: 

    def __init__(self,ancho,alto,profuno):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profuno

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo

cubo = [int(input("Anchura: " if x==0 else "Altura: " if x ==1 else "Profundidad: " )) for x in range(3)]
cubo1 = Cubo(cubo[0],cubo[1],cubo[2])
print(cubo1.calcular_volumen(),"m^3")
