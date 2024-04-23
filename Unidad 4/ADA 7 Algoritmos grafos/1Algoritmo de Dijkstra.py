import heapq

def dijkstra(grafica, inicio):
    distancias = {nodo: float('inf') for nodo in grafica}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafica[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias

grafica = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 6},
    'D': {'B': 1, 'C': 4, 'E': 8},
    'E': {'C': 6, 'D': 8}
}
nodo_inicio = 'A'
print("Distancias más cortas desde el nodo", nodo_inicio)
print(dijkstra(grafica, nodo_inicio))
