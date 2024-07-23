class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def insertar(self, elemento, prioridad):
        self.cola.append((elemento, prioridad))
        self.cola.sort(key=lambda x: x[1])

    def eliminar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)[0]
        else:
            return None

    def esta_vacia(self):
        return len(self.cola) == 0

    def imprimir(self):
        for elemento, prioridad in self.cola:
            print(f"({elemento}, {prioridad})", end=' ')
        print()


cp = ColaPrioridad()

cp.insertar("Tarea 1", 3)
cp.insertar("Tarea 2", 1)
cp.insertar("Tarea 3", 4)
cp.insertar("Tarea 4", 2)
cp.insertar("Tarea 5", 5)

print("Cola de prioridad:")
cp.imprimir()

print("\nEliminando elementos:")
for _ in range(5):
    print(cp.eliminar())