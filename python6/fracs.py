from __future__ import division
import fractions
import unittest


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

class TestStatisticalFunctions(unittest.TestCase):
    def testSkroc(self):
        self.assertEqual(skroc([2, 4]), [1, 2])
        self.assertEqual(skroc([3, 9]), [1, 3])
        self.assertEqual(skroc([15, 3]), [5, 1])
        self.assertRaises(ValueError, skroc, "cos sie...cos sie zepsulo")

    def testAddFrac(self):
        self.assertEqual(add_frac([2, 3], [4, 3]), [2, 1])
        self.assertEqual(add_frac([5, 12], [14, 24]), [1, 1])
    def testSubfrac(self):
        self.assertEqual(sub_frac([2, 3], [4, 3]), [-2, 3])
        self.assertEqual(sub_frac([5, 12], [14, 24]), [-1, 6])
    def testMulfrac(self):
        self.assertEqual(mul_frac([2, 3], [4, 3]), [8, 9])
        self.assertEqual(mul_frac([5, 12], [14, 24]), [35, 144])
    def testDivfrac(self):
        self.assertEqual(div_frac([2, 3], [1, 3]), [2, 1])
        self.assertEqual(div_frac([1, 1], [1, 8]), [8, 1])
        self.assertRaises(ZeroDivisionError, div_frac, [3, 0], [1, 1])
    def testIsPositive(self):
        self.assertFalse(is_positive([-1, 1]))
        self.assertTrue(is_positive([-1, -8]))
        self.assertRaises(ValueError, is_positive, "cos sie...cos sie zepsulo")
    def testIsZero(self):
        self.assertTrue(is_zero([0, 123]))
        self.assertRaises(ValueError, is_zero, "cos sie...cos sie zepsulo")
    def testCmpFrac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
    def frac2float(self):
        self.assertRaises(ValueError, is_positive, 1)
        self.assertEqual(frac2float([1, 2]), 0.5)
