def floyd(grafica):
    distancias = {}
    for u in grafica:
        distancias[u] = {}
        for v in grafica:
            distancias[u][v] = grafica[u].get(v, float('inf'))

    for k in grafica:
        for i in grafica:
            for j in grafica:
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias

grafica = {
    'A': {'B': 2, 'C': 6},
    'B': {'C': 3, 'D': 7},
    'C': {'D': 1},
    'D': {}
}
print("Matriz de distancias mínimas:")
print(floyd(grafica))
