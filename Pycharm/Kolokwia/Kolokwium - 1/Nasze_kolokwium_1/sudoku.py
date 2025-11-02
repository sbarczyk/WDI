T = [
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 3, 6, 8, 8, 9, 6],
    [3, 6, 9, 9, 1, 7, 7, 2, 1],
    [2, 8, 7, 4, 5, 2, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 2, 3, 7],
    [4, 3, 8, 5, 2, 6, 8, 4, 5],
    [7, 9, 6, 3, 1, 8, 1, 6, 9]
]


def check(T):
    # sprawdzanie poprawności wierszy i kolumn:

    for i in range(9):
        tab_1 = [False] * 10
        tab_2 = [False] * 10

        for j in range(9):
            if not tab_1[T[i][j]]:
                tab_1[T[i][j]] = True
            else:
                return False

            if not tab_2[T[j][i]]:
                tab_2[T[j][i]] = True
            else:
                return False

    # sprawdzanie poprawności kwadratów 3x3

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tab_3 = [False] * 10
            for x in range(3):
                for y in range(3):
                    if tab_3[T[x][y]]:
                        return False
                    else:
                        tab_3[T[x][y]] = True

    return True


# zamiana i-tego kwadratu z j-otym
def swap(T, i, j):
    wiersz_i = ((i - 1) // 3) * 3
    kolumna_i = ((i - 1) % 3) * 3

    wiersz_j = ((j - 1) // 3) * 3
    kolumna_j = ((j - 1) % 3) * 3

    for x in range(3):
        for y in range(3):
            temp = T[wiersz_i + x][kolumna_i + y]
            T[wiersz_i + x][kolumna_i + y] = T[wiersz_j + x][kolumna_j + y]
            T[wiersz_j + x][kolumna_j + y] = temp

    return T


def sudoku(T):
    for i in range(1, 9):
        for j in range(i + 1, 10):
            swap(T, i, j)
            if check(T):
                return i, j
            swap(T, i, j)


print(sudoku(T))
