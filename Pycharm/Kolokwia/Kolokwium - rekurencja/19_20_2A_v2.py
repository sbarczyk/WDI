from math import log10, floor


def operation_A(x):
    return x + 3


def operation_B(x):
    return 2 * x


def operation_C(n):
    px = 1
    x = 10
    while n // px > 0:
        if ((n % x) // px) % 2 == 0:
            n += px
        px = x
        x *= 10
    return n


def rek(x, y, n, prev=''):
    if x == y:
        return 1

    if n == 0:
        return 0

    if prev == 'A':
        return rek(operation_B(x), y, n - 1, 'B') + rek(operation_C(x), y, n - 1, 'C')

    elif prev == 'B':
        return rek(operation_A(x), y, n - 1, 'A') + rek(operation_C(x), y, n - 1, 'C')

    elif prev == 'C':
        return rek(operation_A(x), y, n - 1, 'A') + rek(operation_B(x), y, n - 1, 'B')

    else:
        return rek(operation_A(x), y, n - 1, 'A') + rek(operation_C(x), y, n - 1, 'C') + rek(operation_B(x), y, n - 1,
                                                                                             'B')


print(rek(11, 31, 4))
