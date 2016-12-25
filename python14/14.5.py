# -*- coding: utf-8 -*-
from graph import GraphUndirected
from graph import GraphDirected
import random


class GraphCopmplete(GraphUndirected):
    def add_node(self, *nodes):
        for node in nodes:
            lista_tych_samych_elementow_node = [node]*len(self.listnodes())
            edge_list = zip(lista_tych_samych_elementow_node, self.listnodes())

            super(GraphCopmplete, self).add_node(node)

            self.add_edge(*edge_list)


def make_complete(n):
    graph_complete = GraphCopmplete()
    graph_complete.add_node(*range(n))
    return graph_complete

graph = make_complete(3)
graph.print_graph()
print


class GraphCyclic(GraphUndirected):
    def add_node(self, *nodes):
        for node in nodes:
            if len(self._graph_dict) == 0:
                    self._graph_dict[node] = [node]
                    continue
            dowolny_klucz = self._graph_dict.keys()[0]
            lista_sciezek_dowolnego_klucza = self._graph_dict[dowolny_klucz]
            self._graph_dict[dowolny_klucz] = [node]
            self._graph_dict[node] = lista_sciezek_dowolnego_klucza


def make_cyclic(n):
    graph_complete = GraphCyclic()
    graph_complete.add_node(*range(n))
    return graph_complete


graph = make_cyclic(10)
graph.print_graph()
print


class GraphRandomTree(GraphDirected):
    def __init__(self):
        super(GraphRandomTree, self).__init__()
        self.korzen = None

    def add_node(self, *nodes):
        for node in nodes:
            super(GraphRandomTree, self).add_node(node)

            if self.korzen is None:
                self.korzen = node
            else:
                self.rek(self.korzen, node)

    def rek(self, searching_node, new_node):
        if len(self._graph_dict[searching_node]) == 0 or random.randint(0, 100) < 30:
                                                    # 30 - im mniejsza liczba tym drzewo bedzie wyzsze i mniej szerokie
            self._graph_dict[searching_node].append(new_node)
        else:
            self.rek(random.choice(self._graph_dict[searching_node]), new_node)


def make_random_tree(n):
    graph_complete = GraphRandomTree()
    graph_complete.add_node(*range(n))
    return graph_complete

graph = make_random_tree(10)
graph.print_graph()
print
