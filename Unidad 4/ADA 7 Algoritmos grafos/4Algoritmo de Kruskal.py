class ConjuntoDisjunto:
    def __init__(self, vertices):
        self.padre = {vertice: vertice for vertice in vertices}
        self.rango = {vertice: 0 for vertice in vertices}

    def buscar(self, vertice):
        if self.padre[vertice] != vertice:
            self.padre[vertice] = self.buscar(self.padre[vertice])
        return self.padre[vertice]

    def union(self, vertice1, vertice2):
        raiz1 = self.buscar(vertice1)
        raiz2 = self.buscar(vertice2)

        if raiz1 != raiz2:
            if self.rango[raiz1] > self.rango[raiz2]:
                self.padre[raiz2] = raiz1
            else:
                self.padre[raiz1] = raiz2
                if self.rango[raiz1] == self.rango[raiz2]:
                    self.rango[raiz2] += 1

def kruskal(grafica):
    aristas = []
    for vertice in grafica:
        for vecino, peso in grafica[vertice].items():
            aristas.append((peso, vertice, vecino))
    aristas.sort()

    mst = []
    conjunto_disjunto = ConjuntoDisjunto(grafica.keys())

    for arista in aristas:
        peso, vertice1, vertice2 = arista
        if conjunto_disjunto.buscar(vertice1) != conjunto_disjunto.buscar(vertice2):
            mst.append(arista)
            conjunto_disjunto.union(vertice1, vertice2)

    return mst

grafica = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}
print("Arbol de expansión mínimo:")
print(kruskal(grafica))
