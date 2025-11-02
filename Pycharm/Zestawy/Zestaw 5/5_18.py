from math import floor, log10


def last_digit(x):
    return x % 10


def first_digit(x):
    length = floor(log10(x)) + 1
    return x // 10 ** (length - 1)


def is_on_board(n, row, column):
    return 0 <= row < n and 0 <= column < n


def is_move_allowed(from_row, from_column, new_row, new_column, T):
    if is_on_board(8, from_row, from_column) and is_on_board(8, new_row, new_column):
        return last_digit(T[from_row][from_column]) < first_digit(T[new_row][new_column])
    return False


def zad(T):
    n = len(T)

    def rek(row, column):
        moves = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        if row == column == n - 1:
            return True
        for i, j in moves:
            if is_move_allowed(row, column, row + i, column + j, T) and rek(row + i, column + j):
                return True
        return False

    return rek(0, 0)


T = [
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 82, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 91, 2],
    [1, 4, 6, 82, 3, 5, 24, 2],
    [1, 4, 6, 2, 3, 5, 35, 7],
    [1, 4, 6, 2, 3, 5, 35, 8],
]

print(zad(T))
