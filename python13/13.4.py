# -*- coding: utf-8 -*-


def print_sudoku(plansza):
    # +-----+-----+
    print ("+"+5*"-")*2+"+"
    print "| " + str(plansza[3, 0]) + " " + str(plansza[3, 1]) + " | " + str(plansza[3, 2]) + " " + str(plansza[3, 3]) + " |"
    print "| " + str(plansza[2, 0]) + " " + str(plansza[2, 1]) + " | " + str(plansza[2, 2]) + " " + str(plansza[2, 3]) + " |"
    print ("+" + 5 * "-") * 2 + "+"
    print "| " + str(plansza[1, 0]) + " " + str(plansza[1, 1]) + " | " + str(plansza[1, 2]) + " " + str(plansza[1, 3]) + " |"
    print "| " + str(plansza[0, 0]) + " " + str(plansza[0, 1]) + " | " + str(plansza[0, 2]) + " " + str(plansza[0, 3]) + " |"
    print ("+" + 5 * "-") * 2 + "+"


def where_empty(plansza):
    for x in xrange(4):
        for y in xrange(4):
            if plansza[(x, y)] == 0:
                return x, y
    return -1


def empty_plansza():
    plansza = dict()
    for x in xrange(4):
        for y in xrange(4):
            plansza[(x, y)] = 0
    return plansza


def if_good(plansza, xx, yy, value):
    for y in range(yy):  # pionowo
        # (xx,y)
        if plansza[xx, y] == value:
            return False

    for x in range(xx):  # poziomo
        # (x, yy)
        if plansza[x, yy] == value:
            return False
    return True


def sudoku(plansza):
    cords = where_empty(plansza)
    if cords == -1:
        print_sudoku(plansza)
        return


sudoku(empty_plansza())
