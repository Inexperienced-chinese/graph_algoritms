from collections import defaultdict

from base_classes import Graph
from constants import INF
from graph_classes import DirectedGraph


def floyd_warshall_algorithm(graph: Graph, start_node: int, finish_node: int) -> tuple[dict[dict], defaultdict]:
    matrix = build_matrix(graph)
    prevs = defaultdict(dict)
    nodes = graph.nodes.keys()

    for k_node in range(len(nodes)):
        for i_node in nodes:
            for j_node in nodes:

                if k_node in matrix[i_node] and j_node in matrix[k_node]:

                    curr_dist = matrix[i_node][k_node] + matrix[k_node][j_node]

                    if curr_dist < matrix[i_node].get(j_node, INF):
                        matrix[i_node][j_node] = curr_dist
                        prevs[i_node][j_node] = k_node

    return matrix, prevs


def build_matrix(graph: Graph) -> dict[dict]:
    nodes = graph.nodes.keys()
    matrix = defaultdict(dict)

    for i_node in nodes:
        for edge in graph.nodes[i_node].edges:
            matrix[i_node][edge.to_node.num] = edge.weight

    return matrix


graph = DirectedGraph()

graph.insert_edge(1, 2)
graph.insert_edge(2, 3)
graph.insert_edge(3, 4)
graph.insert_edge(4, 1)

print(floyd_warshall_algorithm(graph, 1, 4))
