class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: ¡Guau!")

# Probemos las clases
animal = Animal()
animal.hacer_sonido()

perro = Perro()
perro.hacer_sonido()