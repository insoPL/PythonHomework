# -*- coding: utf-8 -*-

import random


def random_list(n):
    re_list = range(n)
    random.shuffle(re_list)
    return re_list


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item


def not_as_random_list(n):
    re_list = range(n)
    for i in xrange(n-1):
        if random.randint(0, 1):
            swap(re_list, i, i+1)
    return re_list


def not_as_random_list_revert(n):
    re_list = range(n)
    re_list.sort(reverse=True)
    for i in xrange(n-1):
        if random.randint(0, 1):
            swap(re_list, i, i+1)
    return re_list


def gauss_random_list(n):
    re_list = list()
    for i in xrange(n):
        re_list.append(random.gauss(0, 1))
    return re_list


def random_list_from_given_list(n, k):
    """N liczb w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N)."""
    ret_list = list()
    K = range(k)
    for i in xrange(n):
        ret_list.append(random.choice(K))
    return ret_list

lista = gauss_random_list(15)
print lista
