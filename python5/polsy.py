def add_poly(poly1, poly2):
    for x in xrange(len(poly2)):
        try:
         poly1[x]+=poly2[x]
        except IndexError:
            poly1.append(poly2[x])
    return poly1


def sub_poly(poly1, poly2):
    for x in xrange(len(poly2)):
        try:
         poly1[x]-=poly2[x]
        except IndexError:
            poly1.append(-poly2[x])
    return poly1


def is_zero(poly1):
    for x in poly1:
        if x != 0:
            return False
    return True


#  def cmp_poly(poly1, poly2): pass        # bool, porownywanie
#  jak sa rowne to true jak nie to false?

def eval_poly(L, x):
    left=0
    right=len(L)-1
    i = right
    result = L[i]
    while i > left:
        i = i - 1
        result = result * x + L[i]
    return result
