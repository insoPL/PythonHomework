# -*- coding: utf-8 -*-
import random


def random_list_from_given_list(n, k):
    """N liczb w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N)."""
    ret_list = list()
    K = range(k)
    for i in xrange(n):
        ret_list.append(random.choice(K))
    return ret_list


def moda_py(lista):
    apperances = dict()
    for item in lista:
        if item in apperances:
            apperances[item] += 1
        else:
            apperances[item] = 1
    apperances = apperances.items()
    apperances.sort(cmp=lambda a, b: cmp(b[1], a[1]))
    print apperances[0][0]

lista = random_list_from_given_list(20, 10)
print lista

moda = moda_py(lista)

lista.sort()
print lista  # dzieki temu latwiej sprawdzic poprawnosc

print moda
