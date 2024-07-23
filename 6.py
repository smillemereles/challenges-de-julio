class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        
        return nodo

    def imprimir_inorden(self):
        self._imprimir_inorden_recursivo(self.raiz)

    def _imprimir_inorden_recursivo(self, nodo):
        if nodo:
            self._imprimir_inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._imprimir_inorden_recursivo(nodo.derecha)

# Probemos la implementación
arbol = ArbolBinarioBusqueda()
elementos = [5, 3, 7, 1, 9]

for elemento in elementos:
    arbol.insertar(elemento)

print("Árbol en orden:")
arbol.imprimir_inorden()