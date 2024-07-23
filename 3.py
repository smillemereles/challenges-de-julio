def dfs(grafo, nodo_inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo_inicio)
    print(nodo_inicio, end=' ')
    
    for vecino in grafo[nodo_inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Definimos el grafo
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print("Recorrido DFS:")
dfs(grafo, 0)