from base_classes import Graph
from constants import INF
from graph_classes import DirectedGraph


def dijkstra_algorithm(graph: Graph, start_node: int) -> tuple[dict, dict]:
    nodes_count = len(graph.nodes.keys())
    prevs = dict()
    prevs[graph.nodes[start_node]] = None

    used = set()

    distance = dict()
    for node_num in graph.nodes.keys():
        distance[node_num] = INF

    distance[start_node] = 0

    for iteration_num in range(nodes_count):
        curr_node_num = -1

        for node_num in graph.nodes.keys():

            if node_num not in used and (curr_node_num == -1 or distance[node_num] < distance[curr_node_num]):
                curr_node_num = node_num

        if distance[curr_node_num] == INF:
            break

        node = graph.nodes[curr_node_num]
        used.add(curr_node_num)

        for edge in node.edges:
            if distance[edge.to_node.num] > edge.weight + distance[curr_node_num]:
                distance[edge.to_node.num] = edge.weight + distance[curr_node_num]
                prevs[node] = edge.to_node

    return distance, prevs
