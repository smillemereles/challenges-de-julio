class Figura:
    def imprimir(self):
        print("Esta es una figura.")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def imprimir(self):
        print(f"Este es un círculo con radio {self.radio}.")

# Probemos las clases
figura = Figura()
figura.imprimir()

circulo = Circulo(5)
circulo.imprimir()