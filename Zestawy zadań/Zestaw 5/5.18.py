from math import floor, log10

T = [
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 82, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 91, 2],
    [1, 4, 6, 82, 3, 5, 24, 2],
    [1, 4, 6, 2, 3, 5, 35, 7],
    [1, 4, 6, 2, 3, 5, 35, 11],
]


def is_on_board(x, y, n):
    return 0 <= x < n and 0 <= y < n


def can_move_to(from_x, from_y, x, y, T):
    if is_on_board(from_x, from_y, 8) and is_on_board(x, y, 8):
        return get_last(T[from_x][from_y]) < get_first(T[x][y])
    return False


def get_length(n):
    return floor(log10(n)) + 1


def get_first(n):
    length = get_length(n)
    first_digit = n // (10 ** (length - 1))
    return first_digit


def get_last(n):
    return n % 10


def rek(x, y, T):
    moves = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1)]
    if x == 7 and y == 7:
        return True
    for i, j in moves:
        if can_move_to(x, y, x + i, y + j, T):
            return rek(x + i, y + j, T)

    return False


print(rek(0, 0, T))
