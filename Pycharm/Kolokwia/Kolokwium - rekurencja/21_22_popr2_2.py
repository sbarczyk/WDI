from math import sqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, int(sqrt(x)) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True


def komnaty(T):
    def rek(i, s):  # i - nr indeksu komnaty, s - ilosc sztabek z jaka do tej komnaty wchodzimy
        if i == len(T) - 1:
            return T[i] + s <= 100 and is_prime(T[i] + s)

        # x - ilosc sztabek jaką zostawimy w tej komnacie
        for x in range(s - 6, s + 1):
            if 1 < T[i] + x <= 100 and is_prime(T[i] + x):
                if rek(i + 1, s - x):
                    return True
        return False

    return rek(0, 0)


print(komnaty([10, 20, 35]))
print(komnaty([10, 20, 30]))
