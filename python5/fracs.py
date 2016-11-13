from __future__ import division
import fractions


def skroc(frac):
    nwd = fractions.gcd(*frac)
    frac[0] /= nwd
    frac[1] /= nwd
    return frac


def add_frac(frac1, frac2):
    frac1[0] *= frac2[1]
    frac2[0] *= frac1[1]
    frac1[1] *= frac2[1]


    return skroc([frac1[0]+frac2[0], frac1[1]])


def sub_frac(frac1, frac2):
    frac1[0] *= frac2[1]
    frac2[0] *= frac1[1]
    frac1[1] *= frac2[1]

    print frac1, frac2
    return skroc([frac1[0]-frac2[0], frac1[1]])


def mul_frac(frac1, frac2):
    frac1[0] *= frac2[0]
    frac1[1] *= frac2[1]
    return skroc(frac1)


def div_frac(frac1, frac2):
    frac1[0] *= frac2[1]
    frac1[1] *= frac2[0]
    return skroc(frac1)


def is_positive(frac):
    if frac[0]*frac[1] > 0: return True
    else: return False


def is_zero(frac):
    if frac[0] == 0: return True
    else: return False


def cmp_frac(frac1, frac2):
    w = sub_frac(frac1, frac2)
    if is_positive(w): return 1
    elif is_zero(w): return 0
    else: return -1


def frac2float(frac):
    return float(frac[0]/frac[1])
