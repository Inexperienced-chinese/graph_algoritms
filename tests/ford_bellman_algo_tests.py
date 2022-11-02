from math import inf
import unittest
from ford_bellman_algo import ford_bellman_algo
from graph_classes import DirectedGraph

def create_graph_from_test(edges):
    graph = DirectedGraph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])
    return graph


class FordBellmanAlgoTests(unittest.TestCase):
    def test1_graph_without_neg_widths(self):
        graph_in_edge = [
             (1, 2, 2), (1, 3, 6), (1, 4, 1), (1, 6, 7), (2, 1, 2), (2, 3, 3),
             (2, 6, 4), (3, 4, 4), (4, 5, 2), (5, 3, 1)
          ]
        graph = create_graph_from_test(graph_in_edge)

        node_min_width_ans = {1: 0, 2: 2, 3: 4, 4: 1, 5: 3, 6: 6}
        node_ancestor_ans = {2: 1, 3: 5, 4: 1, 5: 4, 6: 2}

        node_min_width, node_ancestor = ford_bellman_algo(graph, 1)
        for node, ans in node_min_width_ans.items():
            self.assertEqual(ans, node_min_width[node])
        for node, ans in node_ancestor_ans.items():
            self.assertEqual(ans, node_ancestor[node])

    def test1_graph_with_neg_widths(self):
        graph_in_edge = [
            (1, 2, 5), (1, 3, -4), (3, 4, 6), (4, 2, 2), (4, 1, -1)
        ]
        graph = create_graph_from_test(graph_in_edge)

        node_min_width_ans = {1: 0, 2: 4, 3: -4, 4: 2}
        node_ancestor_ans = {2: 4, 3: 1, 4: 3}

        node_min_width, node_ancestor = ford_bellman_algo(graph, 1)
        for node, ans in node_min_width_ans.items():
            self.assertEqual(ans, node_min_width[node])
        for node, ans in node_ancestor_ans.items():
            self.assertEqual(ans, node_ancestor[node])

    def test1_graph_with_neg_cycle(self):
        graph_in_edge = [
            (1, 2, -1), (1, 5, 6), (2, 3, 2), (2, 4, -4), (3, 2, -3), (4, 3, 4),
            (5, 6, 3), (6, 2, -7), (6, 4, -10), (6, 5, 2)
        ]
        graph = create_graph_from_test(graph_in_edge)

        node_min_width_ans = {1: 0, 2: -inf, 3: -inf, 4: -inf, 5: 6, 6: 9}
        node_ancestor_ans = {2: 3, 3: 4, 4: 2, 5: 1, 6: 5}

        node_min_width, node_ancestor = ford_bellman_algo(graph, 1)
        for node, ans in node_min_width_ans.items():
            self.assertEqual(ans, node_min_width[node])
        for node, ans in node_ancestor_ans.items():
            self.assertEqual(ans, node_ancestor[node])
