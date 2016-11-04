# 4.3
x="xD"

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

