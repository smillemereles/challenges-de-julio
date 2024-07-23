def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Probemos la función
lista_desordenada = [64, 25, 12, 22, 11]
lista_ordenada = ordenamiento_seleccion(lista_desordenada)
print("Lista ordenada:", lista_ordenada)