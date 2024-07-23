def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))

# Probemos la función
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
lista_sin_duplicados = eliminar_duplicados(lista_con_duplicados)

print("Lista original:", lista_con_duplicados)
print("Lista sin duplicados:", lista_sin_duplicados)