def warshall(grafica):
    n = len(grafica)
    cierre_transitivo = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            cierre_transitivo[i][j] = grafica[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cierre_transitivo[i][j] = cierre_transitivo[i][j] or (cierre_transitivo[i][k] and cierre_transitivo[k][j])

    return cierre_transitivo

grafica = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]
print("Cierre transitivo del grafo:")
print(warshall(grafica))
