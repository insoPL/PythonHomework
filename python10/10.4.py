# -*- coding: utf-8 -*-
import unittest


class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):             # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):             # nigdy nie jest pusta
        return False

    def put(self, data):
        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise IndexError
        return self.items.pop(0)   # mało wydajne!


class TestStackClass(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())

    def test_put(self):
        self.assertIsNone(self.queue.put(1))
        self.assertIsNone(self.queue.put(5))
        self.assertIsNone(self.queue.put(6))
        self.assertIsNone(self.queue.put(13))

    def test_get(self):
        self.queue.put(1)
        self.queue.put(5)
        self.queue.put(6)
        self.queue.put(13)

        self.assertEqual(self.queue.get(), 1)
        self.assertEqual(self.queue.get(), 5)
        self.assertEqual(self.queue.get(), 6)
        self.assertEqual(self.queue.get(), 13)
        self.assertRaises(IndexError, self.queue.get)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.put(1)
        self.assertFalse(self.queue.is_empty())

    def test_str(self):
        self.assertEqual(str(self.queue), "[]")
        self.queue.put(1)
        self.assertEqual(str(self.queue), "[1]")
