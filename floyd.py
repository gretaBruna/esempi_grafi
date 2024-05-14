import networkx as nx

G = nx.DiGraph()
G.add_weighted_edges_from([(0, 1, 5), (1, 2, 2),
                           (2, 3, -3), (1, 3, 10),
                           (3, 2, 8)])
fw = nx.floyd_warshall(G, weight="weight")
for a, b in fw.items():
    print(a)
    print(b)

results = {a: dict(b) for a, b in fw.items()}
print(results)