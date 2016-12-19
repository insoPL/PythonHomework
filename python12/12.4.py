# -*- coding: utf-8 -*-
import random


def random_list_from_given_list(n, k):
    """N liczb w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N)."""
    ret_list = list()
    K = range(k)
    for i in xrange(n):
        ret_list.append(random.choice(K))
    return ret_list


def dominata(lista):
    lista.sort()
    maximum = 0
    previous_item = None
    apperance_counter = None
    for current_item in lista:
        if current_item != previous_item:
            maximum = max(maximum, apperance_counter)
            apperance_counter = 1
        else:
            apperance_counter += 1
        previous_item = current_item
    maximum = max(maximum, apperance_counter)

    return maximum


lista = random_list_from_given_list(20, 10)
lista = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 6, 7, 7, 9, 9, 9]
print lista
moda = dominata(lista)
lista.sort()
print lista
print moda
