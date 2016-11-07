# 4.2


def linijkarz(dl):
    st = "|...." * dl + "|\n0"
    for it in range(1, dl + 1):
        st += "{0:5d}".format(it)
    return st


def kwadratura(x, y):
    return ("+---" * x + "+\n" + "|   " * x + "|\n") * y + "+---" * x + "+\n"


# 4.3


def factorial(n):
    suma = 1
    for x in range(n):
        suma += suma * x
    return suma


# 4.4


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    pop = 1
    pop2 = 1
    for n in xrange(n - 2):
        tym = pop
        pop = pop + pop2
        pop2 = tym
    return pop


# 4.5


# noinspection PyPep8Naming
def odwracanie(L, left, right):
    tym = L[left-1]
    L[left-1] = L[right-1]
    L[right-1] = tym

    if right - left <= 1:
        return L
    else:
        return odwracanie(L, left + 1, right - 1)


# noinspection PyPep8Naming
def odwracanieit(L, left, right):
    left -= 1
    right -= 1
    while right - left > 1:
        tym = L[left]
        L[left] = L[right]
        L[right] = tym
        right -= 1
        left += 1
    return L

# 4.6


def sum_seq(sequence):
    suma = 0
    for it in sequence:
        if isinstance(it, (list, tuple)):
            suma += sum_seq(it)
        else:
            suma += it
    return suma


# 4.7


def flatten(sequence):

    seq = list()

    for it in sequence:
        if isinstance(it, (list, tuple)):
            seq += flatten(it)
        else:
            seq.append(it)
    return seq


S = [range(2), 5, 1, 2, [2], (4, [1, 2, 3])]

print flatten(S)