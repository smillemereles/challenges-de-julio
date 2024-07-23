class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def describir(self):
        return f"Motor {self.tipo} de {self.potencia} HP"

class Auto:
    def __init__(self, marca, modelo, tipo_motor, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor, potencia_motor)
    
    def describir_auto(self):
        print(f"Este es un {self.marca} {self.modelo}")
        print(f"Equipado con: {self.motor.describir()}")

# Probemos las clases
mi_auto = Auto("Toyota", "Corolla", "Gasolina", 150)
mi_auto.describir_auto()