from math import inf
from typing import Tuple, Dict
from base_classes import Graph, Node, Edge
from collections import deque


def levit_algo(self: Graph, start_node: int) -> Tuple[Dict[int, int], Dict[int, int]]:
    node_min_width = {}
    for node in self.nodes:
        node_min_width[node] = inf
    node_min_width[start_node] = 0

    node_ancestor = {}

    M0 = set()
    M1 = deque([start_node])
    M2 = set()
    for node in self.nodes:
        if node != start_node:
            M2.add(node)


    while len(M1) != 0:
        curr_node = M1.popleft()
        M0.add(curr_node)
        for edge in self.nodes[curr_node].edges:
            to_node = edge.to_node.num
            if to_node in M2:
                M2.remove(to_node)
                node_min_width[to_node] = node_min_width[curr_node] + edge.weight
                node_ancestor[to_node] = curr_node
                M1.append(to_node)
            elif to_node in M0:
                if node_min_width[curr_node] + edge.weight < node_min_width[to_node]:
                    node_min_width[to_node] = node_min_width[curr_node] + edge.weight
                    node_ancestor[to_node] = curr_node
                    M0.remove(to_node)
                    M1.appendleft(to_node)
            else:
                if node_min_width[curr_node] + edge.weight < node_min_width[to_node]:
                    node_min_width[to_node] = node_min_width[curr_node] + edge.weight
                    node_ancestor[to_node] = curr_node

    return node_min_width, node_ancestor
