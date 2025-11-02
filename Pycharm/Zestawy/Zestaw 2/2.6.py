from math import sqrt
def iloczyn_liczby(n):
    best = n-1
    iloczyn = (n, 1)
    for i in range (1, int(sqrt(n) + 1)):
        if n%i == 0:
            roznica = abs(i - n//i)
            if roznica < best:
                roznica = best
                iloczyn = (i, n//i)
    return iloczyn

print(iloczyn_liczby(120))