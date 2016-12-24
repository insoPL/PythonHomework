# -*- coding: utf-8 -*-

from graph import GraphUndirected


class GraphCopmplete(GraphUndirected):
    def add_node(self, *nodes):
        for node in nodes:
            if node in self.graph_dict:
                return
            lista_tych_samych_elementow_node = [node]*len(self.listnodes())
            edge_list = zip(lista_tych_samych_elementow_node, self.listnodes())

            if node not in self.graph_dict:
                self.graph_dict[node] = []

            print edge_list
            self.add_edge(*edge_list)

graph_complete = GraphCopmplete()

graph_complete.add_node("A", "B", "C", "D", "E")

print
graph_complete.print_graph()
