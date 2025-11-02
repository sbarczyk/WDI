from math import isqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x) + 1, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True



def check(T):
    n = len(T)
    iloczyn = 0
    max_index = None

    for i in range(n):
        if is_prime(T[i]):
            if iloczyn == 0:
                iloczyn = T[i]
            else:
                iloczyn *= T[i]
        elif iloczyn ==  T[i]:
                max_index = i
    return max_index

print(check([2,3,9,6]))