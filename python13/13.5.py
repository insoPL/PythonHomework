# -*- coding: utf-8 -*-


def print_sudoku(plansza):
    global suma
    suma += 1
    if suma % 1000 != 0: #  wypisz co tysieczną plansze
        return None
    # +-----+-----+
    print ("+" + 5 * "-") * 3 + "+"
    print "| " + str(plansza[0, 5]) + " " + str(plansza[1, 5]) + " | " + str(plansza[2, 5]) + " " + str(plansza[3, 5]) + " | " + str(plansza[4, 5]) + " " + str(plansza[5, 5]) + " |"
    print "| " + str(plansza[0, 4]) + " " + str(plansza[1, 4]) + " | " + str(plansza[2, 4]) + " " + str(plansza[3, 4]) + " | " + str(plansza[4, 4]) + " " + str(plansza[5, 4]) + " |"
    print "| " + str(plansza[0, 3]) + " " + str(plansza[1, 3]) + " | " + str(plansza[2, 3]) + " " + str(plansza[3, 3]) + " | " + str(plansza[4, 3]) + " " + str(plansza[5, 3]) + " |"
    print ("+" + 5 * "-") * 3+ "+"
    print "| " + str(plansza[0, 2]) + " " + str(plansza[1, 2]) + " | " + str(plansza[2, 2]) + " " + str(plansza[3, 2]) + " | " + str(plansza[4, 2]) + " " + str(plansza[5, 2]) + " |"
    print "| " + str(plansza[0, 1]) + " " + str(plansza[1, 1]) + " | " + str(plansza[2, 1]) + " " + str(plansza[3, 1]) + " | " + str(plansza[4, 1]) + " " + str(plansza[5, 1]) + " |"
    print "| " + str(plansza[0, 0]) + " " + str(plansza[1, 0]) + " | " + str(plansza[2, 0]) + " " + str(plansza[3, 0]) + " | " + str(plansza[4, 0]) + " " + str(plansza[5, 0]) + " |"
    print ("+" + 5 * "-") * 3 + "+"
    print suma
    print


def where_empty(plansza):
    for x in xrange(6):
        for y in xrange(6):
            if plansza[(x, y)] == 0:
                return x, y
    return -1


def empty_plansza():
    plansza = dict()
    for x in xrange(6):
        for y in xrange(6):
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
    yk = yy/3  # yk = codry malego kwadraciku
    for x in xrange(2):
        for y in xrange(3):
            if plansza[(xk*2)+x, (yk*3)+y] == value:
                return False

    return True


def sudoku(plansza):
    cords = where_empty(plansza)
    if cords == -1:
        print_sudoku(plansza)
        return
    else:
        x, y = cords
        for i in xrange(1, 7):
            if if_good(plansza, i, *cords):
                plansza[cords] = i
                sudoku(plansza.copy())

suma = 0
sudoku(empty_plansza())
