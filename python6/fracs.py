from __future__ import division
import fractions
import unittest


class Frac:
    """Klasa reprezentujaca ulamek."""

    def check(self):
        if self.y == 0:
            raise ZeroDivisionError
        if not isinstance(self, Frac) or not isinstance(self.x, int) or not isinstance(self.y, int):
            raise ValueError

    def skroc(self):
        nwd = fractions.gcd(self.x, self.y)
        self.x = int(self.x / nwd)
        self.y = int(self.y / nwd)

    def __init__(self, x=0, y=1):
        if isinstance(x, Frac):
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y
        self.check()
        self.skroc()
        if self.y < 0:
            self.y *= -1
            self.x *= -1

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        return str(self.x)+"/"+str(self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other):  # frac1 + frac2
        other.check()
        other.skroc()

        xx = other.x

        foo = Frac(self)

        foo.x *= other.y
        foo.y *= other.y
        xx *= self.y

        foo.x += xx
        foo.skroc()
        return foo

    def __sub__(self, other):  # frac1 - frac2
        other.check()
        other.skroc()
        xx = other.x

        foo = Frac(self)

        foo.x *= other.y
        foo.y *= other.y
        xx *= self.y

        print foo, xx

        foo.x -= xx
        foo.skroc()
        return foo

    def __mul__(self, other):  # frac1 * frac2
        other.check()
        other.skroc()

        foo = Frac(self)

        foo.x *= other.x
        foo.y *= other.y
        foo.skroc()
        return foo

    def __truediv__(self, other):  # frac1 / frac2
        return self*(~other)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return Frac(self)

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):  # cmp(frac1, frac2)
        wyn = float(self-other)
        if wyn > 0:
            return 1
        if wyn == 0:
            return 0
        if wyn < 1:
            return -1

    def __float__(self):      # float(frac)
        return float(self.x/self.y)


class TestFracsClass(unittest.TestCase):

    def testInit(self):
        self.assertEqual(Frac(3, 2), Frac(3, 2))
        self.assertEqual(Frac(6, 4), Frac(3, 2))
        self.assertEqual(Frac(15, 3), Frac(25, 5))
        self.assertEqual(Frac(-15, 4), Frac(15, -4))
        self.assertRaises(ZeroDivisionError, Frac, 12, 0)
        self.assertRaises(ValueError, Frac, ["xD", "Niskie"])

    def testAdd(self):
        self.assertEqual(Frac(2, 3) + Frac(4, 3), Frac(2, 1))
        self.assertEqual(Frac(1, 12) + Frac(14, 24), Frac(2, 3))
        self.assertRaises(ZeroDivisionError, Frac, 12, 0)
        self.assertRaises(ValueError, Frac, ["xD", "Niskie"])

    def testSub(self):
        self.assertEqual(Frac(2, 3) - Frac(4, 3), Frac(-2, 3))
        self.assertEqual(Frac(1, 12) - Frac(14, 24), Frac(-1, 2))
        self.assertRaises(ZeroDivisionError, Frac, 12, 0)
        self.assertRaises(ValueError, Frac, ["xD", "Niskie"])

    def testMul(self):
        self.assertEqual((Frac(2, 3) * Frac(4, 3)), Frac(8, 9))
        self.assertEqual((Frac(5, 12) * Frac(14, 24)), Frac(35, 144))
        self.assertRaises(ZeroDivisionError, Frac, 12, 0)
        self.assertRaises(ValueError, Frac, ["xD", "Niskie"])

    def testDiv(self):
        self.assertEqual((Frac(2, 3) / (Frac(1, 3))), Frac(2, 1))
        self.assertEqual((Frac(1, 1) / Frac(1, 8)), Frac(8, 1))
        self.assertRaises(ZeroDivisionError, Frac, 12, 0)
        self.assertRaises(ValueError, Frac, ["xD", "Niskie"])

    def testCMP(self):
        self.assertTrue(Frac(2, 1) > Frac(1, 2))
        self.assertTrue(Frac(1, -2) < Frac(-1, 3))
        self.assertRaises(ZeroDivisionError, Frac, 12, 0)
        self.assertRaises(ValueError, Frac, ["xD", "Niskie"])
