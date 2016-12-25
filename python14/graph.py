# -*- coding: utf-8 -*-

# wykorzystuje kod oparty na na słowniku tak jak jest w przykładzie z dokumentacji


class Graph(object):
    def __init__(self):
        self._graph_dict = {}

    def add_node(self, *nodes):
        """Wstawia wierzchołek do grafu."""
        for node in nodes:
            if node not in self._graph_dict:
                self._graph_dict[node] = []

    def listnodes(self):
        """Zwraca listę wierzchołków grafu."""
        return self._graph_dict.keys()

    def listedges(self):
        """Zwraca listę krawędzi (krotek) grafu."""
        L = []
        for source in self._graph_dict:
            for target in self._graph_dict[source]:
                L.append((source, target))
        return L
    
    def print_graph(self):
        """Wypisuje postać grafu na ekranie."""
        for source in self._graph_dict:
            print source, ":",
            for target in self._graph_dict[source]:
                print target,
            print


class GraphDirected(Graph):
    def add_edge(self, *edges):
        """Dodaje krawędź do grafu skierowanego."""
        for edge in edges:
            source, target = edge
            if source not in self._graph_dict.keys() or target not in self._graph_dict.keys():
                raise ValueError("sciezka miedzy nie istniejącymi punktami")
            # Możemy wykluczyć pętle.
            if source == target:
                raise ValueError("pętle są zabronione")
            if target not in self._graph_dict[source]:
                self._graph_dict[source].append(target)


class GraphUndirected(Graph):
    def add_edge(self, *edges):
        """Dodaje krawędź do grafu nieskierowanego."""
        for edge in edges:
            source, target = edge
            if source not in self._graph_dict.keys() or target not in self._graph_dict.keys():
                raise ValueError("sciezka miedzy nie istniejącymi punktami")
            # Możemy wykluczyć pętle.
            if source == target:
                raise ValueError("pętle są zabronione")
            if target not in self._graph_dict[source]:
                self._graph_dict[source].append(target)
            if source not in self._graph_dict[target]:
                self._graph_dict[target].append(source)
