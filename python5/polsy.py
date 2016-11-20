import unittest


def add_poly(poly1, poly2):
    ret1 = list(poly1)
    for x in xrange(len(poly2)):
        try:
            ret1[x] += poly2[x]
        except IndexError:
            ret1.append(poly2[x])
    return ret1


def sub_poly(poly1, poly2):
    ret1 = list(poly1)
    for x in xrange(len(poly2)):
        try:
            ret1[x] -= poly2[x]
        except IndexError:
            ret1.append(-poly2[x])
    return ret1


def is_zero(poly1):
    for x in poly1:
        if x != 0:
            return False
    return True


#  def cmp_poly(poly1, poly2): pass        # bool, porownywanie
#  jak sa rowne to true jak nie to false?

def eval_poly(L, x):
    left = 0
    right = len(L)-1
    i = right
    result = L[i]
    while i > left:
        i -= 1
        result = result * x + L[i]
    return result


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x*x

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertTrue(is_zero(sub_poly(self.p1,  self.p1)))
        self.assertTrue(is_zero(sub_poly(self.p2,  self.p2)))
        self.assertEqual(sub_poly(self.p1,   self.p2),  [0, 1, -1])

    def test_mul_poly(self): pass

    def test_is_zero(self): pass

    def test_cmp_poly(self): pass

    def test_eval_poly(self): pass

    def test_combine_poly(self): pass

    def test_pow_poly(self): pass

    def test_diff_poly(self): pass

    def tearDown(self): pass
