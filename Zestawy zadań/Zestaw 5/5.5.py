from math import sqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, int(sqrt(x)) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True


def to_decimal(T):
    res = 0
    n = len(T)
    for i in range(n):
        res += T[i] * (2 ** (n - i - 1))
    return res


def zad5(T):
    def rek(i, j, T):
        if j > len(T) - 1:
            return False
        if j == len(T) - 1:
            return is_prime(to_decimal(T[i:j + 1]))
        if is_prime(to_decimal(T[i:j + 1])):
            rek(j + 1, j + 2, T)

        return rek(i, j + 1, T)

    return rek(0, 1, T) if len(T) > 1 else False


T = [1, 1, 0, 1, 0, 0]
print(zad5(T))
