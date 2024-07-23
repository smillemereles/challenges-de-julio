import math

class FormaGeometrica:
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Probemos las clases
rectangulo = Rectangulo(5, 3)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")

circulo = Circulo(4)
print(f"Área del círculo: {circulo.calcular_area():.2f}")
print(f"Perímetro del círculo: {circulo.calcular_perimetro():.2f}")