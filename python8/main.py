# -*- coding: utf-8 -*-
import random
import math

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    aa = a/-b
    cc = c/-b #aax + cc=y
    return a+c/-b


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    pi = 0
    for i in xrange(n):
        x = (random.randrange(-10000, 10000)/10000.0)
        y = (random.randrange(-10000, 10000)/10000.0)
        if x*x +y*y <= 1:
            pi+=1
    print pi* 4.0 / n

calc_pi()

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a+b <= c or a+c <= b or b+c <= a or a<0 or b<0 or c<0:
        raise ValueError
    p = 1.0/2.0 * (a+b+c)
    print math.sqrt(p*(p-a)*(p-b)*(p-c))

heron(3, 3, 3)


def P(a, b):
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

def P_dynamic(a, b):
    P_dict = dict()

    if a < 0 or b < 0:
        raise ValueError
    for sum in xrange(max(a, b)):
        for aa in xrange(min(sum, a+1)):
            for bb in xrange(min(sum, b+1)):
                print "[", aa, ", ", bb, "]"
                if aa == 0 and bb == 0:
                    P_dict[aa, bb] = 0.5
                elif aa > 0 and bb == 0:
                    P_dict[aa, bb] = 0
                elif aa == 0 and bb > 0:
                    P_dict[aa, bb] = 1,
                elif aa > 0 and bb > 0:
                    print "WTF"
                    P_dict[aa, bb] = (P_dict[aa - 1, bb] + P_dict[aa, bb - 1])
    return P_dict[a, b]

#for i in xrange(10):
 #   for j in xrange(10):
  #      print P_dynamic(i, j)
print P_dynamic(2,2)