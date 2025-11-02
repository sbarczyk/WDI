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


def zad(T):
    n = len(T)
    max_ind = None
    iloczyn = 0
    for i, element in enumerate(T):
        if is_prime(element):
            if iloczyn == 0:
                iloczyn = element
            else:
                iloczyn *= element
        elif iloczyn == element:
            max_ind = i
    return max_ind


T = [1, 2, 3, 8, 10, 11, 66]
print(zad(T))
