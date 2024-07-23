class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

    def imprimir(self):
        print("Pila:", self.items)

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def imprimir(self):
        print("Cola:", self.items)

#  implementaciones
pila = Pila()
cola = Cola()

print("Operaciones con Pila:")
for i in range(1, 6):
    pila.push(i)
    pila.imprimir()

print("\nDesapilando:")
for _ in range(5):
    print(pila.pop())

print("\nOperaciones con Cola:")
for i in range(1, 6):
    cola.encolar(i)
    cola.imprimir()

print("\nDesencolando:")
for _ in range(5):
    print(cola.desencolar())