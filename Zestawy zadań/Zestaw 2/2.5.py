from math import log10, floor
def get_leng(n):
    return floor(log10(n)) + 1

def nowa_liczba(n, mask):
    liczba = i = 0
    while n > 0:
        if mask % 2 == 0:
            pass
        else:
            liczba += (n%10) * 10 ** i
            i += 1
        mask //= 2
        n //= 10
    return liczba

def zad(n):
    for mask in range (1, 2**get_leng(n)):
        liczba = nowa_liczba(n, mask)
        if liczba % 7 == 0:
            print(liczba)

zad(2315)


