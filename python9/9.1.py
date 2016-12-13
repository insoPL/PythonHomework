# -*- coding: utf-8 -*-class Node:


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

lista = Node(0)
for i in xrange(1, 20):
    lista = Node(i, lista)


def print_list(node):
    while node:
        print node.data
        node = node.next


def delete_head(node):
    return node.next, node.data


def remove_tail(node):
    new_head = node
    while node.next.next:
        node = node.next
    data = node.next.data
    node.next = None
    return new_head, data


lista, _ = delete_head(lista)
lista, _ = remove_tail(lista)
print_list(lista)
