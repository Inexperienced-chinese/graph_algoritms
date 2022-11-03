from base_classes import Graph


class UnDirectedGraph(Graph):
    def __init__(self):
        self.nodes = {}


    def add_edge(self, from_node_num: int, to_node_num: int, weight: int = 1):
        self.insert_node(from_node_num)
        self.insert_node(to_node_num)

        self.nodes[from_node_num].add_edge_to_node(self.nodes[to_node_num], weight)
        self.nodes[to_node_num].add_edge_to_node(self.nodes[from_node_num], weight)


class DirectedGraph(Graph):
    def __init__(self):
        self.nodes = {}

    def add_edge(self, from_node_num: int, to_node_num: int, weight: int = 1):
        self.insert_node(from_node_num)
        self.insert_node(to_node_num)

        self.nodes[from_node_num].add_edge_to_node(self.nodes[to_node_num], weight)
