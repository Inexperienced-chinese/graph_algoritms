from math import inf
from base_classes import Graph, Node, Edge


def ford_bellman_algo(self: Graph, start_node: int):
    node_min_width = {}
    for node in self.nodes:
        node_min_width[node] = inf
    node_min_width[start_node] = 0

    node_ancestor = {}

    for i in range(len(self.nodes) - 1):
        for node in self.nodes:
            for edge in self.nodes[node].edges:
                if node_min_width[edge.to_node.num] > node_min_width[node] + edge.weight:
                    node_min_width[edge.to_node.num] = node_min_width[node] + edge.weight
                    node_ancestor[edge.to_node.num] = node

    for node in self.nodes:
        for edge in self.nodes[node].edges:
            if node_min_width[edge.to_node.num] > node_min_width[node] + edge.weight:
                node_min_width[edge.to_node.num] = -inf

    return node_min_width, node_ancestor
