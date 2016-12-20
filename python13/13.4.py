# -*- coding: utf-8 -*-


def print_sudoku(plansza):
    global suma
    # +-----+-----+
    print ("+"+5*"-")*2+"+"
    print "| " + str(plansza[3, 0]) + " " + str(plansza[3, 1]) + " | " + str(plansza[3, 2]) + " " + str(plansza[3, 3]) + " |"
    print "| " + str(plansza[2, 0]) + " " + str(plansza[2, 1]) + " | " + str(plansza[2, 2]) + " " + str(plansza[2, 3]) + " |"
    print ("+" + 5 * "-") * 2 + "+"
    print "| " + str(plansza[1, 0]) + " " + str(plansza[1, 1]) + " | " + str(plansza[1, 2]) + " " + str(plansza[1, 3]) + " |"
    print "| " + str(plansza[0, 0]) + " " + str(plansza[0, 1]) + " | " + str(plansza[0, 2]) + " " + str(plansza[0, 3]) + " |"
    print ("+" + 5 * "-") * 2 + "+"
    print suma
    print
    suma += 1


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


def if_good(plansza, value, xx, yy):
    for y in range(yy):  # pionowo
        # (xx,y)
        if plansza[xx, y] == value:
            return False

    for x in range(xx):  # poziomo
        # (x, yy)
        if plansza[x, yy] == value:
            return False

    # w kwadraciku
    xk = xx/2
    yk = yy/2  # yk = codry malego kwadraciku
    for x in xrange(2):
        for y in xrange(2):
            if plansza[(xk*2)+x, (yk*2)+y] == value:
                return False
    return True


def sudoku(plansza, deep):
    cords = where_empty(plansza)
    deep -= 1
    if cords == -1 or deep == -1:
        print_sudoku(plansza)
        return
    else:
        x, y = cords
        for i in xrange(1, 5):
            if if_good(plansza, i, *cords):
                plansza[cords] = i
                sudoku(plansza.copy(), deep)

suma = 1
sudoku(empty_plansza(), 16)
