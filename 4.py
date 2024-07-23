from collections import deque

def bfs(grafo, nodo_inicio):
    visitados = set()
    cola = deque([nodo_inicio])
    visitados.add(nodo_inicio)
    
    while cola:
        nodo = cola.popleft()
        print(nodo, end=' ')
        
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

# Usamos el mismo grafo definido anteriormente
print("\nRecorrido BFS:")
bfs(grafo, 0)