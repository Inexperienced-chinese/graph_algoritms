from typing import List

from constants import INF
from graph_classes import DirectedGraph


PARAMS = [
        [
            'graph_without_neg_widths',
            [
                (1, 2, 2), (1, 3, 6), (1, 4, 1), (1, 6, 7), (2, 1, 2), (2, 3, 3),
                (2, 6, 4), (3, 4, 4), (4, 5, 2), (5, 3, 1)
            ],
            {1: 0, 2: 2, 3: 4, 4: 1, 5: 3, 6: 6},
            {2: 1, 3: 5, 4: 1, 5: 4, 6: 2}
        ],
        [
            'graph_with_neg_widths',
            [(1, 2, 5), (1, 3, -4), (3, 4, 6), (4, 2, 2), (4, 1, -1)],
            {1: 0, 2: 4, 3: -4, 4: 2},
            {2: 4, 3: 1, 4: 3}
        ],
        [
            'graph_with_neg_cycle',
            [
                (1, 2, -1), (1, 5, 6), (2, 3, 2), (2, 4, -4), (3, 2, -3), (4, 3, 4),
                (5, 6, 3), (6, 2, -7), (6, 4, -10), (6, 5, 2)
            ],
            {1: 0, 2: -INF, 3: -INF, 4: -INF, 5: 6, 6: 9},
            {2: 3, 3: 4, 4: 2, 5: 1, 6: 5}
        ]
    ]


def create_graph_from_test(edges):
    graph = DirectedGraph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])
    return graph


def get_params(param_names: List[str]):

    params = [param for param in PARAMS if param[0] in param_names]

    return params
