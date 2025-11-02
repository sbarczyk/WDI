from math import isqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True


def rek(n, result=0, pos=0, flag=False):
    if n == 0:
        if result > 9 and flag and is_prime(result):
            print(result)
        return
    rek(n // 10, result, pos, True)
    rek(n // 10, result + ((n % 10) * 10 ** pos), pos + 1, flag)


rek(311)
