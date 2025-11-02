tab = [
    [3, 11, 14, 17],
    [6, 12, 7, 9],
    [10, 8, 16, 13],
    [5, 15, 4, 2]
]


def wiersz_w_prawo(tab, row):
    n = len(tab)
    temp = tab[row][n - 1]

    for i in range(n - 1, 0, -1):
        tab[row][i] = tab[row][i - 1]

    tab[row][0] = temp

    return tab


def kolumna_w_dol(tab, col):
    n = len(tab)
    temp = tab[-1][col]

    for i in range(n - 1, 0, -1):
        tab[i][col] = tab[i - 1][col]

    tab[0][col] = temp
    return tab


def check(tab):
    suma = 0
    for i in range(len(tab)):
        suma += tab[0][i]

    for x in range(len(tab)):
        suma1 = 0
        suma2 = 0
        for y in range(len(tab)):
            suma1 += tab[x][y]
            suma2 += tab[y][x]

        if suma1 != suma or suma2 != suma:
            return False

    return True


def magic(tab):
    def rek(tab, l_oper):
        if l_oper == 2:
            return check(tab)

        for i in range(len(tab)):
            new_tab = [row[:] for row in tab]
            wiersz_w_prawo(new_tab, i)
            if rek(new_tab, l_oper + 1):
                return True

            new_tab = [row[:] for row in tab]
            kolumna_w_dol(new_tab, i)
            if rek(new_tab, l_oper + 1):
                return True

        return False

    return rek(tab, 0)


print(magic(tab))
