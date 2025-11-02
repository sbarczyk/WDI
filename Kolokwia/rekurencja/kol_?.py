# król na polu (0,0), ma się dostać na (n-1, n-1) jak najniższym kosztem. Ruchy tylko w prawo i w dół


T = [
    [0, 5, 4, 3],
    [2, 1, 3, 2],
    [8, 2, 5, 1],
    [4, 3, 2, 0]
]


def zad(T):
    n = len(T)

    def rek(T, row, col):
        if row == n - 1 and col == n - 1:
            return T[row][col]
        if row > n - 1 or col > n - 1:
            return float('inf')

        return min(rek(T, row + 1, col), rek(T, row, col + 1)) + T[row][col]

    return rek(T, 0, 0)


print(zad(T))
