# -*- coding: utf-8 -*-

from graph import Graph

graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")

graph.print_graph()
print

graph.add_edge_undirected(("A", "B"), ("B", "C"), ("C", "D"))


graph.print_graph()