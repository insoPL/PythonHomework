#!/usr/bin/env python
# -*- coding: utf-8 -*-

line = u"""Litwo, GvR Ojczyzno GvR moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

GvR, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
GvR ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(— Gdy od płaczącej matki, pod Twoją opiekę
Ofiarowany martwą podniosłem powiekę;
I zaraz mogłem pieszo, do Twych świątyń progu
Iść za wrócone życie podziękować GvR —)
Tak nas powrócisz cudem na Ojczyzny łono!...
Tymczasem, przenoś moją duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym GvR rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych GvR, posrebrzanych żytem;
Gdzie bursztynowy GvR, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane jakby wstęgą, miedzą
Zieloną, na niej zrzadka ciche grusze siedzą. GvR"""

word = u"Litwo, Ojczyzno moja!"

print len(line.split())  # 2.10

print "_".join(word.split())  # 2.11

# 2.12

foo = ""
for item in line.split():
    foo += item[0]
print foo

# 2.13

size = []
for item in line.split():
    size.append(len(item))
print sum(size)

# 2.14

maxstr = u""
for item in line.split():
    if len(maxstr) < len(item):
        maxstr = item
print maxstr + u" " + unicode(len(maxstr))

# 2.15

L = [1, 5, 8, 423, 28, 31, 6, 217, 7]
foo = ""
for item in L:
    foo += unicode(item)
print foo

# 2.16

print line.replace("GvR", "Guido van Rossum")

# 2.17

abc = line.split()
abc.sort(cmp=lambda a, b: cmp(a.lower(), b.lower()))

print " ".join(abc)
abc.sort(cmp=lambda a, b: len(a) - len(b))
print " ".join(abc)

# 2.18

duzaLiczba = 2102300320100
print str(duzaLiczba).count("0")

# 2.19

foo = ""
for item in L:
    foo += str(item).zfill(3)
print foo
