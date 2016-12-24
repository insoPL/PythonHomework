# -*- coding: utf-8 -*-


class Graph(object):
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, *nodes):
        """Wstawia wierzchołek do grafu."""
        for node in nodes:
            if node not in self.graph_dict:
                self.graph_dict[node] = []

    def listnodes(self):
        """Zwraca listę wierzchołków grafu."""
        return self.graph_dict.keys()

    def listedges(self):
        """Zwraca listę krawędzi (krotek) grafu."""
        L = []
        for source in self.graph_dict:
            for target in self.graph_dict[source]:
                L.append((source, target))
        return L
    
    def print_graph(self):
        """Wypisuje postać grafu na ekranie."""
        for source in self.graph_dict:
            print source, ":",
            for target in self.graph_dict[source]:
                print target,
            print


class GraphDirected(Graph):
    def add_edge(self, *edges):
        """Dodaje krawędź do grafu skierowanego."""
        for edge in edges:
            source, target = edge
            self.add_node(source)
            self.add_node(target)
            # Możemy wykluczyć pętle.
            if source == target:
                raise ValueError("pętle są zabronione")
            if target not in self.graph_dict[source]:
                self.graph_dict[source].append(target)


class GraphUndirected(Graph):
    def add_edge(self, *edges):
        """Dodaje krawędź do grafu nieskierowanego."""
        for edge in edges:
            source, target = edge
            self.add_node(source)
            self.add_node(target)
            # Możemy wykluczyć pętle.
            if source == target:
                raise ValueError("pętle są zabronione")
            if target not in self.graph_dict[source]:
                self.graph_dict[source].append(target)
            if source not in self.graph_dict[target]:
                self.graph_dict[target].append(source)
