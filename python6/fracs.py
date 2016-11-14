from __future__ import division
import fractions
import unittest


class Frac:
    """Klasa reprezentujaca ulamek."""

    def _check(self, *arg):
        if self.y == 0:
            raise ZeroDivisionError
        if not isinstance(check.x, int) or not isinstance(check.y, int):
            raise ValueError
        for foo in arg:
            if foo.y == 0:
                raise ZeroDivisionError
            if not isinstance(foo, Frac) or not isinstance(foo.x, int) or not isinstance(foo.y, int):
                raise ValueError

    def _skroc(self):
        nwd = fractions.gcd(self.x, self.y)
        self.x = int(self.x / nwd)
        self.y = int(self.y / nwd)

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        check()
        skroc()
        if y < 0:
            y *= -1
            x *= -1

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        return str(self.x)+"/"+str(self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other):  # frac1 + frac2
        check(other)
        self.x *= other.y
        other.x *= self.y
        self.y *= other.y

        self.x += other.x
        check()

    def __sub__(self, other):  # frac1 - frac2
        check(other)
        self.x *= other.y
        other.x *= self.y
        self.y *= other.y

        self.x -= other.x
        check()

    def __mul__(self, other): pass  # frac1 * frac2

    def __div__(self, other): pass  # frac1 / frac2

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other): pass  # cmp(frac1, frac2)

    def __float__(self): pass       # float(frac)

def skroc(frac):
    check(frac)

    nwd = fractions.gcd(*frac)
    frac[0] = int(frac[0] / nwd)
    frac[1] = int(frac[1] / nwd)

    return frac

def check(*arg):
    for frac in arg:
        if frac[1] == 0:
            raise ZeroDivisionError
        if not isinstance(frac, list) or not isinstance(frac[0], int) or not isinstance(frac[1], int):
            raise ValueError

def add_frac(frac1, frac2):
    check(frac1, frac2)

    frac1[0] *= frac2[1]
    frac2[0] *= frac1[1]
    frac1[1] *= frac2[1]

    return skroc([frac1[0]+frac2[0], frac1[1]])


def sub_frac(frac1, frac2):
    check(frac1, frac2)

    frac1[0] *= frac2[1]
    frac2[0] *= frac1[1]
    frac1[1] *= frac2[1]

    print frac1, frac2
    return skroc([frac1[0]-frac2[0], frac1[1]])


def mul_frac(frac1, frac2):
    check(frac1, frac2)

    frac1[0] *= frac2[0]
    frac1[1] *= frac2[1]
    return skroc(frac1)


def div_frac(frac1, frac2):
    check(frac1, frac2)

    frac1[0] *= frac2[1]
    frac1[1] *= frac2[0]
    return skroc(frac1)


def is_positive(frac):
    check(frac)

    if frac[0]*frac[1] > 0: return True
    else: return False


def is_zero(frac):
    check(frac)

    if frac[0] == 0: return True
    else: return False


def cmp_frac(frac1, frac2):
    check(frac1, frac2)
    w = sub_frac(frac1, frac2)
    if is_positive(w): return 1
    elif is_zero(w): return 0
    else: return -1


def frac2float(frac):
    check(frac)

    return float(frac[0]/frac[1])


class TestFracsClass(unittest.TestCase):


    def testSkroc(self):
        self.assertEqual(Frac(6,4)._skroc(self),Frac(3,2))
