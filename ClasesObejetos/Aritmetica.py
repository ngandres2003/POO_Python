class Aritmetica:
    """
    clase Aritmetica para realizar las operaciones 
    matematicas
    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA +  self.operandoB
    def resta(self):
        return self.operandoA -  self.operandoB
    def multiplicar(self):
        return self.operandoA *  self.operandoB
    def dividir(self):
        return self.operandoA /  self.operandoB
        


aritmetica1 = Aritmetica(10,2)
print(aritmetica1.sumar())
print(aritmetica1.resta())
print(aritmetica1.multiplicar())
print(aritmetica1.dividir())

