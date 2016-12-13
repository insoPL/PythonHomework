# -*- coding: utf-8 -*-
import unittest


class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pełny
        return False

    def push(self, item):
        if self.is_full():
            raise IndexError
        self.items.append(item)         # dodajemy na koniec

    def pop(self):   # zwraca element
        if self.is_empty():
            raise IndexError
        return self.items.pop()         # zabieram od końca


class TestStackClass(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())

    def test_push(self):
        self.assertIsNone(self.stack.push(1))
        self.assertIsNone(self.stack.push(5))
        self.assertIsNone(self.stack.push(6))
        self.assertIsNone(self.stack.push(13))

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(13)

        self.assertEqual(self.stack.pop(), 13)
        self.assertEqual(self.stack.pop(), 6)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.pop(), 1)
        self.assertRaises(IndexError, self.stack.pop)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_str(self):
        self.assertEqual(str(self.stack), "[]")
        self.stack.push(1)
        self.assertEqual(str(self.stack), "[1]")
