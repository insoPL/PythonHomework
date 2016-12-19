# -*- coding: utf-8 -*-
import random

def random_list_from_given_list(n, k):
    """N liczb w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N)."""
    ret_list = list()
    K = range(k)
    for i in xrange(n):
        ret_list.append(random.choice(K))
    return ret_list

lista = random_list_from_given_list(20, 10)
lista.sort()
print lista
