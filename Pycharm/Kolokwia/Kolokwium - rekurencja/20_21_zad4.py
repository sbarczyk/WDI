from math import isqrt, floor, log10


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True


def divide(n, cnt=0):
    if n == 0:
        if is_prime(cnt):
            return True
        else:
            return False

    length = floor(log10(n)) + 1

    for i in range(1, length + 1):
        prefix = n // (10 ** (length - i))
        new_n = n % (10 ** (length - i))
        if is_prime(prefix):
            if divide(new_n, cnt + 1):
                return True
    return False


print(divide(2222))
print(divide(22222))
