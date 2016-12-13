# -*- coding: utf-8 -*-

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def create_tree(deep):
    if deep == 0:
        return Node(deep)
    deep -= 1
    node = Node(deep+1, create_tree(deep), create_tree(deep))
    return node

tree = create_tree(3)


def count_leafs(top):
    if top is None:
        return 0
    elif top.left is None and top.right is None:
        return 1
    add = 0
    add += count_leafs(top.left)
    add += count_leafs(top.right)
    return add


def calc_total(top):
    if top is None:
        return 0
    add = top.data
    add += calc_total(top.left)
    add += calc_total(top.right)
    return add
print "calc", calc_total(tree)
