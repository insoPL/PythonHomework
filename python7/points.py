import unittest
import math
import copy

class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __deepcopy__(self, memodict={}):
        not_there = []
        existing = memodict.get(self, not_there)
        if existing is not not_there:
            return existing
        dup = Point(copy.deepcopy(self.x, memodict), copy.deepcopy(self.y, memodict))
        memodict[self] = dup
        return dup

    def __str__(self):         # zwraca string "(x, y)"
        return "("+str(self.x)+", "+str(self.y)+")"

    def __repr__(self): # zwraca string "Point(x, y)"
        return "Point("+str(self.x)+", "+str(self.y)+")"

    def __eq__(self, other):   # obsluga point1 == point2
        if not isinstance(other, Point):
            other = Point(other)
        if other.x == self.x and other.y == self.y:
            return True
        else:
            return False

    def __ne__(self, other):        # obsluga point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        if not isinstance(other, Point):
            Point(other)
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):  # v1 - v2
        if not isinstance(other, Point):
            Point(other)
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):          # dlugosc wektora
        return math.sqrt(self.x*self.x+self.y*self.y)

# Kod testujacy modul.


class TestPoint(unittest.TestCase):
    def testStr(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertEqual(str(Point(4, 1)), "(4, 1)")
        self.assertEqual(Point(1, 2).__repr__(), "Point(1, 2)")
        self.assertEqual(Point(4, 1).__repr__(), "Point(4, 1)")

    def testComp(self):
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertNotEqual(Point(1, 2), Point(2, 1))

    def testAdd(self):
        self.assertEqual(Point(1, 2)+Point(1, 2), Point(2, 4))
        self.assertEqual(Point(-1, 6)+Point(4, -4), Point(3, 2))

    def testSub(self):
        self.assertEqual(Point(1, 2)-Point(1, 2), 0)
        self.assertEqual(Point(-1, 6)-Point(4, -4), Point(-5, 10))

    def testLength(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(4, 3).length(), 5)

    def testSkalar(self):
        self.assertEqual(Point(1, 2) * Point(4, -2), 0)
