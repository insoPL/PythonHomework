# -*- coding: utf-8 -*-
import random


def random_list_from_given_list(n, k):
    """N liczb w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N)."""
    ret_list = list()
    K = range(k)
    for i in xrange(n):
        ret_list.append(random.choice(K))
    return ret_list


def moda_sort(lista):
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
print lista

moda = moda_sort(lista)

lista.sort()
print lista  # dzieki temu latwiej sprawdzic poprawnosc

print moda
