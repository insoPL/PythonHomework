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


def quicksort(L, left, right, compare=cmp):
    if left >= right:
        return
    swap(L, left, (left + right) / 2)   # element podziału
    pivot = left                      # przesuń do L[left]
    for i in range(left + 1, right + 1):   # podział
        if compare(L[i], L[left]) < 0:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

lista = random_list(16)
quicksort(lista, 0, 15)
print lista
