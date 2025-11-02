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

def czy_komplementarne(a,b):
    suma = a + b
    return is_prime(suma)

def zad13(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            flag = False
            for x in range(n):
                for y in range(n):
                    if i == x and j == y:
                        continue
                    if T[x][y] == 0:
                        continue
                    if czy_komplementarne(T[i][j], T[x][y]):
                        flag = True
                        break
            if not flag:
                T[i][j] = 0
    return T

tab = [ [2,3], [3,12] ]
print( zad13(tab) )



