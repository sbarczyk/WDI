from math import isqrt

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x)+1, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True

def eval(T):
    suma = 0
    n = len(T)
    for i in range(0, n//2*2, 2):
        suma += T[i] * T[i+1]

    if n % 2 == 1:
        suma += T[n-1]
    return suma

def find_max(T):
    maks = 0
    n = len(T)
    for i in range(n-1):
        for j in range(i+1, n):
            if i == 0 and j == n-1:
                continue
            e = eval(T[i:j+1])
            if is_prime(e):
                maks = max(maks, e/len(T[i:j+1]))
            e = T[i] + eval(T[i+1:j+1])
            if is_prime(e):
                maks = max(maks, e/len(T[i:j+1]))

    return maks

print(find_max([7, 8, 6, 4, 7, 3]))