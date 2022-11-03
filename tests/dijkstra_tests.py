import unittest

from graph_algorithms.dijkstra_algorithm import dijkstra_algorithm
from graph_algorithms.ford_bellman_algo import ford_bellman_algo
from parameterized import parameterized

from tests.utils import create_graph_from_test, get_params


class DijkstraAlgoTests(unittest.TestCase):
    @parameterized.expand(get_params(['graph_without_neg_widths']))
    def tests(self, test_name, graph_in_edge, node_min_width_ans, node_ancestor_ans):
        graph = create_graph_from_test(graph_in_edge)

        node_min_width, node_ancestor = dijkstra_algorithm(graph, 1)
        for node, ans in node_min_width_ans.items():
            self.assertEqual(ans, node_min_width[node], f'failed in test {test_name}')
        for node, ans in node_ancestor_ans.items():
            self.assertEqual(ans, node_ancestor[node])
