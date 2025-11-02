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

def find_sequence(tab):
    diff = tab[1] - tab[0]
    max_len = curr_len = 2

    for i in range(2, len(tab)):
        if tab[i] - tab[i-1] == diff and is_prime(tab[i]) and is_prime(tab[i-1]):
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            diff = tab[i] - tab[i-1]
            curr_len = 2
    return max_len

def find_longest_sequence(T):
    n = len(T)
    max_lenght = 0
    for x in range(n):
        max_lenght = max(max_lenght, find_sequence(T[x])), find_longest_sequence(T[j][x] for j in range(n))
    return max_lenght