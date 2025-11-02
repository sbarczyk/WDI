# Król który porusza się z pola (n-1, n-1) tylko w górę lub w lewo. Każde pole ma swój koszt. Znajdź drogę z
# najniższym kosztem.

def zad(T):
    n = len(T)

    def rek(T, row, col):
        if row == 0 and col == 0:
            return 0
        if row < 0 or col < 0:
            return float('inf')

        return min(rek(T, row - 1, col), rek(T, row, col - 1)) + T[row][col]

    return rek(T, n - 1, n - 1)


T = [
    [0, 5, 4, 3],
    [2, 1, 3, 2],
    [8, 2, 5, 1],
    [4, 3, 2, 0]
]
print(zad(T))
