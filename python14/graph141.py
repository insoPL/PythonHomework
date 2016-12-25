# -*- coding: utf-8 -*-

# realizuje zadanie 14.1
# nie moglem nazwac pliku "14.1" poniwaz potrzebowalem go do importu

# wykorzystuje kod oparty na na słowniku z przykładu z dokumentacji


class Graph(object):
    def __init__(self):
        self._graph_dict = {}

    def add_node(self, *nodes):
        """Wstawia wierzchołek do grafu."""
        for node in nodes:
            if node not in self._graph_dict:
                self._graph_dict[node] = []

    def list_nodes(self):
        """Zwraca listę wierzchołków grafu."""
        return self._graph_dict.keys()

    def count_nodes(self):
        """Zwraca liczbę wierzchołków"""
        return len(self.list_nodes())

    def list_edges(self):
        """Zwraca listę krawędzi (krotek) grafu."""
        L = []
        for source in self._graph_dict:
            for target in self._graph_dict[source]:
                L.append((source, target))
        return L

    def count_edges(self):
        """Zwraca liczbę krawędzi grafu"""
        return len(self.list_edges())

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
