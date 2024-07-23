def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return False

# Probemos la función
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
numero_buscado = 13

if busqueda_binaria(lista_ordenada, numero_buscado):
    print(f"El número {numero_buscado} está en la lista.")
else:
    print(f"El número {numero_buscado} no está en la lista.")