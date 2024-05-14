import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.directed_havel_hakimi_graph([3] * 15,
                                   [3] * 15,
                                   create_using=None)

for v in G.edges():
    G[v[0]][v[1]]['weight'] = random.randrange(1,10)


print(G.nodes())
print(G.edges())
# nx.draw(G, with_labels=True, font_weight='bold')

pos=nx.spring_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

print(nx.dijkstra_path(G, 0, 7))
print(nx.dijkstra_path_length(G, 0, 7))

optpath = nx.dijkstra_path(G, 0, 7)
optedges = []
for i in range(0, len(optpath)-1):
    optedges.append([optpath[i], optpath[i+1]])


nx.draw_networkx_edges(G, pos, optedges, edge_color="red")

plt.savefig("plot")
plt.show()