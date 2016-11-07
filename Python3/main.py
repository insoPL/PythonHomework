# import sys

# 3.1
x, y = 2, 3

if x > y:
    result = x
else:
    result = y
print result
print

# 3.2

# L.sort()

# x, y = 1, 2

# X = [1, 2, 3]
# X[1] = 4

# X = [1, 2, 3]
# X[3] = 4

# X = "abc"
# X=X+"d"

# map(pow, range(8), range(8))

# 3.3

for it in range(30):
    if it % 3:
        print it
print

# 3.4

while True:
    # reply = raw_input("Podaj liczbe:")
    reply = "stop"
    if reply == "stop":
        break
    try:
        number = int(reply)
    except ValueError:
        print "To nie jest liczba!"
    else:
        print [number, pow(number, 3)]
print

# 3.5

dl = 5

st = "|...." * dl + "|\n0"
for it in range(1, dl + 1):
    st += "{0:5d}".format(it)
print st

# 3.6

x, y = 6, 2

st = ("+---" * x + "+\n" + "|   " * x + "|\n") * y + "+---" * x + "+\n"

print st

# 3.8

A = [2, 4, 6, 8, 10, 12]
B = [3, 6, 9, 12, 15]

AUB = list(A)  # suma obu zbiorow
AUB += B
AUB.sort()
AUB = list(set(AUB))  # usuniecie duplikatow
print AUB

AWB = []
for a in A:
    for b in B:
        if a == b:
            AWB.append(a)
AWB.sort()
AWB = list(set(AWB))  # usuniecie duplikatow

print AWB

# 3.9
W = list()
A = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

for a in A:
    W.append(sum(a))
print W

# 3.10
D = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman2int(stri):
    """zmienia liczbe zapisana cyframi rzymskim na cyfry arabskie"""
    if len(stri) == 0:
        return 0
    elif len(stri) == 1:
        return D[stri]

    else:
        maximum = 0
        for bar in stri:  # znajdz najwiekszy znak - maximum
            if D[bar] > maximum:
                maximum = D[bar]

        xx = 0
        for bar in stri:  # znajdz taki najwiekszy ktory stoi najbardziej z lewej - xx
            if D[bar] == maximum:
                break
            else:
                xx += 1

        return roman2int(stri[xx + 1:]) + D[stri[xx]] - roman2int(stri[0:xx])
        # to co znajdziesz na lewo od xx odejmij od xx a to co na prawo dodaj


print
print

print roman2int("MMMCCCXXXVIII")
