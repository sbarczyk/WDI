from math import isqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 3 == 0 or x % 2 == 0:
        return False
    for i in range(6, isqrt(x) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True


def divide(n):
    def rek(n, i, cnt):
        if is_prime(n) and is_prime(cnt):
            return True
        if i > n:
            return False
        if is_prime(n % i):
            if rek(n // i, 10, cnt + 1):
                return True
        return rek(n, i * 10, cnt)

    return rek(n, 10, 1)


print(divide(23672))
