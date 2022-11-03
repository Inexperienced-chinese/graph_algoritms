from graph_classes import DirectedGraph, UnDirectedGraph

graph = UnDirectedGraph()

for i in range(5):
    graph.insert_node(i + 1)

graph.insert_edge(1, 2)

graph.insert_edge(134, 676, weight=67)

for k, v in graph.nodes.items():
    print(k, v)
