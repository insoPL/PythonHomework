# -*- coding: utf-8 -*-
import unittest
import time


def P(a, b):  # 1 000 w ponad 2 min
    if a < 0 or b < 0:
        raise ValueError
    elif a == 0 and b == 0:
        return 0.5
    elif a > 0 and b == 0:
        return 0
    elif a == 0 and b > 0:
        return 1
    else:
        return 0.5 * (P(a - 1, b) + P(a, b - 1))


def P_dynamic(a, b):  # 10 000 w 20 sek
    P_dict = dict()

    if a < 0 or b < 0:
        raise ValueError
    for aa in xrange(a+1):
        for bb in xrange(b+1):
            if aa == 0 and bb == 0.0:
                P_dict[aa, bb] = 0.5
            elif aa > 0 and bb == 0:
                P_dict[aa, bb] = 0.0
            elif aa == 0 and bb > 0:
                P_dict[aa, bb] = 1.0
            elif aa > 0 and bb > 0:
                P_dict[aa, bb] = (P_dict[aa - 1, bb] + P_dict[aa, bb - 1]) * 0.5
    return P_dict[a, b]


class TimeComp(unittest.TestCase):
    def setUp(self):
        self.input_data = list()
        for i in xrange(13):
            for j in xrange(13):
                self.input_data.append((i, j))
        self.start_time = time.time()

        self.wyniki_rek = list()
        self.wyniki_dyn = list()

    def tearDown(self):
        t = time.time() - self.start_time
        print "Czas przeprowadzanie testu %s trwa: %.3f" % (self.shortDescription(), t)

    def test_rekurencyjny(self):
        """metody rekurencyjnej"""
        for krotka in self.input_data:
            self.wyniki_rek.append(P(*krotka))

    def test_dynamiczny(self):
        """metody dynamicznej"""
        for krotka in self.input_data:
            self.wyniki_dyn.append(P_dynamic(*krotka))

    def test_danych_wyjscia(self):
        """zgodnosci danych w obu metodach"""
        for krotka in self.input_data:
            self.wyniki_rek.append(P(*krotka))

        for krotka in self.input_data:
            self.wyniki_dyn.append(P_dynamic(*krotka))

        wyniki = zip(self.wyniki_dyn, self.wyniki_rek)
        for odp1, odp2 in wyniki:
            self.assertEqual(odp1, odp2)
