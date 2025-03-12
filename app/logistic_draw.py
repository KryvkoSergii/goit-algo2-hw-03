# The algorithm of Emondsa-Karpa and the maximum potency of the network
import networkx as nx
import matplotlib.pyplot as plt
from logistic_data import edges, positions

G = nx.DiGraph()

G.add_weighted_edges_from(edges)

plt.figure(figsize=(10, 6))
nx.draw(G, positions, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, positions, edge_labels=labels)

print(G.number_of_edges())
plt.show()
