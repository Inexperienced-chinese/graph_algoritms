from __future__ import annotations

import abc


class Edge:
    def __init__(self, weight: int, to_node: Node):
        self.weight = weight
        self.to_node = to_node

    def __repr__(self):
        return f'Edge to: {self.to_node.num}, weight={self.weight}'


class Node:
    def __init__(self, node_num, edges: list[Edge]):
        self.num = node_num
        self.edges = edges[::]

    def add_edge(self, to_node: Node, weight):
        self.edges.append(Edge(weight, to_node))

    def __repr__(self):
        return f'Node{self.num}: {self.edges}'


class Graph(abc.ABC):
    nodes = {}

    @abc.abstractmethod
    def add_edge(self, from_node_num: int, to_node_num: int, weight: int = 0):
        pass

    def insert_node(self, node_num: int = None):
        if node_num not in self.nodes.keys():
            self.nodes[node_num] = Node(node_num, [])
            return True

        return False
