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


def number_length(x):
    return floor(log10(x)) + 1


def unique_digits(x):
    T = [False] * 10
    while x != 0:
        if T[x % 10]:
            return False
        else:
            T[x % 10] = True
            x //= 10
    return True


def obciecie(num):
    L = number_length(num)
    M = 0
    maxi = 0

    while num != 0:
        cp_num = num

        while cp_num != 0:
            if unique_digits(cp_num) and is_prime(cp_num):
                maxi = max(maxi, cp_num)

            cp_num //= 10

        M += 1
        num = num % 10 ** (L - M)

    return maxi


print(obciecie(1202742516))
