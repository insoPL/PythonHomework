from points import Point
import unittest
import math


class Circle:
    """Klasa reprezentujaca okregi na plaszczyznie."""

    def __init__(self, x=0, y=0, radius=1):

        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __deepcopy__(self, memodict={}):
        return Point(self.pt.x, self.pt.y, self.radius)

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle("+str(self.pt.x)+", "+str(self.pt.y)+", "+str(self.radius)+")"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi*math.pow(self.radius, 2)

    def move(self, x, y):
        return Circle(self)

    def cover(self, other): pass   # okrag pokrywajacy oba


class TestCircle(unittest.TestCase):
    def testInit(self):
        self.assertIsInstance(Circle(), Circle)

    def testCmp(self):
        self.assertEqual(Circle(2, 2, 2), Circle(2, 2, 2))

    def testStr(self):
        self.assertEqual(Circle(2, 2, 2).__repr__(), "Circle(2, 2, 2)")

    def testArea(self):
        self.assertAlmostEqual(Circle().area(), 3.14, delta=0.1)
        self.assertAlmostEqual(Circle(5, 4, 3).area(), 28.27, delta=0.1)


