import networkx as nx
import itertools
import matplotlib.pyplot as plt

G = nx.DiGraph()

estados = ["CDMX", "Jalisco", "Nuevo León", "Querétaro", "Veracruz", "Yucatán", "Chiapas"]
for estado in estados:
    G.add_node(estado)

G.add_edge("CDMX", "Jalisco", weight=500)
G.add_edge("CDMX", "Nuevo León", weight=700)
G.add_edge("CDMX", "Querétaro", weight=200)
G.add_edge("Jalisco", "Veracruz", weight=800)
G.add_edge("Nuevo León", "Yucatán", weight=1000)
G.add_edge("Querétaro", "Chiapas", weight=600)
G.add_edge("Veracruz", "Yucatán", weight=900)
G.add_edge("Yucatán", "Chiapas", weight=400)
G.add_edge("Chiapas", "CDMX", weight=750)

print("Recorrido sin repetir estados:")
hamiltonian_path = None
for perm in itertools.permutations(estados):
    if all(perm[i] != perm[i+1] for i in range(len(perm)-1)):
        if perm[-1] != perm[0]:
            continue
        if all(G.has_edge(perm[i], perm[i+1]) for i in range(len(perm)-1)):
            hamiltonian_path = perm
            break

if hamiltonian_path:
    total_cost = sum(G[hamiltonian_path[i]][hamiltonian_path[i+1]]['weight'] for i in range(len(hamiltonian_path)-1))
    print(" -> ".join(hamiltonian_path), "Costo:", total_cost)
else:
    print("No se encontró un recorrido sin repetir estados")

print("\nRecorrido con repetición de estados:")
try:
    path_with_repeat = list(nx.simple_cycles(G))[0] 
    total_cost = sum(G[path_with_repeat[i]][path_with_repeat[i+1]]['weight'] for i in range(len(path_with_repeat)-1))
    total_cost += G[path_with_repeat[-1]][path_with_repeat[0]]['weight'] 
    print(" -> ".join(path_with_repeat + [path_with_repeat[0]]), "Costo:", total_cost)
except nx.NetworkXNoPath:
    print("No se encontró un recorrido con repetición de estados")

print("\nCosto de ir a cada estado desde cualquier estado:")
for estado_inicio in estados:
    print(f"\nCosto desde {estado_inicio}:")
    for estado_destino in estados:
        if estado_inicio != estado_destino:
            try:
                shortest_path = nx.shortest_path(G, source=estado_inicio, target=estado_destino)
                total_cost = nx.shortest_path_length(G, source=estado_inicio, target=estado_destino, weight='weight')
                print(f"  A {estado_destino}: {total_cost}")
            except nx.NetworkXNoPath:
                print(f"  No hay ruta a {estado_destino} desde {estado_inicio}")

print("\nRelaciones de estados en el grafo:")
for edge in G.edges(data=True):
    print(f"{edge[0]} -> {edge[1]}, Costo: {edge[2]['weight']}")

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo de Estados de la República Mexicana')
plt.show()