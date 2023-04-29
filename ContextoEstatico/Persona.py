class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas
    
    def __init__(self,nombre,edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Persona [{self.id_persona} {self.nombre} {self.edad}]"
    
persona_1 = Persona("Andres",20)
print(persona_1)

persona_2 = Persona("Jennire", 19)
print(persona_2)

print(Persona.contador_personas)

persona_3 = Persona("Carlos",24)
print(persona_3)

print(Persona.contador_personas)

Persona.generar_siguiente_valor()
print(Persona.contador_personas)