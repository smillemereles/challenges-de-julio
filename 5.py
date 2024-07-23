import heapq

def dijkstra(grafo, inicio, fin):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    pq = [(0, inicio)]
    camino = {}
    
    while pq:
        distancia_actual, nodo_actual = heapq.heappop(pq)
        
        if nodo_actual == fin:
            break
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                camino[vecino] = nodo_actual
                heapq.heappush(pq, (distancia, vecino))
    
    return distancias, camino

# Definimos el grafo con pesos
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

inicio, fin = 'A', 'E'
distancias, camino = dijkstra(grafo, inicio, fin)

print(f"\nLa distancia más corta de {inicio} a {fin} es: {distancias[fin]}")

# Reconstruir el camino
ruta = []
while fin:
    ruta.append(fin)
    fin = camino.get(fin)
ruta.reverse()

print("El camino más corto es:", ' -> '.join(ruta))