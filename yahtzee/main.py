import matplotlib.pyplot as plt
import networkx as nx

from graph import Graph
from node import DecisionNode, RollNode

# [x] DONE Warmup-Game MicroYahtzee (2-Fields: Double, Square, 1 Player)
# [ ] ---- extend to: + Rerolls
# [ ] ---- extend to: + 2 Players
# [ ] ---- extend to: + More Dice (Combinatorics)

init_state = RollNode(frozenset({'D', 'S', 'A'}))

yahtzee_graph = Graph(init_state)
G = yahtzee_graph.graph

yahtzee_graph.build_graph()
yahtzee_graph.calculate_evs()
# Find optimum decision for state: { free fields }

plt.figure(figsize=(18, 18))

G.graph['graph'] = {'rankdir': 'LR'}
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')

print(yahtzee_graph.decision_nodes)
nx.draw_networkx_nodes(G, pos, yahtzee_graph.decision_nodes, node_shape='s', node_color='w', edgecolors='black')
nx.draw_networkx_nodes(G, pos, yahtzee_graph.roll_nodes, node_shape='o', node_color='w', edgecolors='black',
                       node_size=400)
node_labels = dict([(n, f"{n.describe_simple()}") for n in G.nodes])
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)

nx.draw_networkx_edges(G, pos, G.edges)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, rotate=False, font_size=6, label_pos=0.7)

print(yahtzee_graph.optimal_edges)
nx.draw_networkx_edges(G, pos, yahtzee_graph.optimal_edges, edge_color='red')

# plt.axis('off')
plt.show()

# plt.savefig("plot.png", dpi=300)
