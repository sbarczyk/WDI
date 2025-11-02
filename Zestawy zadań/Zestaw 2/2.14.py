from math import sqrt, floor, log10

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, int(sqrt(x) + 1), 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True

def get_length(x):
    return floor(log10(x)) + 1

def validate_mask(leng1, leng2, mask):
    while mask > 0:
        if mask % 2 == 0:
            leng1 -= 1
        else:
            leng2 -= 1

        mask //= 2

    return leng1 >= 0 and leng2 == 0


def nowa_liczba(a, b, mask):
    nowa_liczba = 0
    mult = 1

    while mask > 0 or a > 0 or b > 0:
        if mask % 2 == 0:
            d = a % 10
            a //= 10
        else:
            d = b % 10
            b //= 10

        mask //= 2

        nowa_liczba = d * mult + nowa_liczba
        mult *= 10

    return nowa_liczba

def zad(a, b):
    counter = 0
    leng_a, leng_b = get_length(a), get_length(b)
    for mask in range(2 ** (leng_a + leng_b)):
        if validate_mask(leng_a, leng_b, mask) and is_prime(nowa_liczba(a, b, mask)):
            print(nowa_liczba(a,b, mask))
            counter += 1
    return counter

print(zad(121, 73))
