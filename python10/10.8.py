# -*- coding: utf-8 -*-
import random


class RandomQueue:

    def __init__(self):
            self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):   # zwraca losowy element
        rand = random.randint(0, len(self)-1)
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def __len__(self):
        return len(self.items)

    def is_full(self):             # nigdy nie jest pusta
        return False

    def __str__(self):             # podglądanie kolejki
        return str(self.items)


randomQueue = RandomQueue()
randomQueue.insert(3)
randomQueue.insert(7)
randomQueue.insert(1)
randomQueue.insert(4)

print randomQueue.remove()
