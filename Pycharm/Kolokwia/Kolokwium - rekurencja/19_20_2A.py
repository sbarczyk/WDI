from math import log10


def operation_C(a):
    b = 0
    length = int(log10(a)) + 1
    for i in range(length - 1, -1, -1):
        n = (a // 10 ** i) % 10
        if n % 2 == 0:
            b = b * 10 + (n + 1)
        else:
            b = b * 10 + n
    return b


def zad2A(X, Y, N):
    def rek(x, y, n, prev):
        if x == y:
            return 1
        if n == 0:
            return 0
        return (
                (0 if prev == 'A' else rek(x + 3, y, n - 1, 'A')) +
                (0 if prev == 'B' else rek(x * 2, y, n - 1, 'B')) +
                (0 if prev == 'C' else rek(operation_C(x), y, n - 1, 'C'))
        )

    return rek(X, Y, N, None)


print(zad2A(11, 31, 4))
