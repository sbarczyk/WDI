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


def zad(A, B):
    num = 2 ** (A + B - 1)
    suma = 0

    def rek(A, B, num):
        nonlocal suma
        if A == B == 0:
            if not is_prime(num):
                suma += 1
                print(num)
            return

        if A > 0:
            rek(A - 1, B, num + 2 ** (A + B - 1))

        if B > 0:
            rek(A, B - 1, num)

    rek(A - 1, B, num)
    return suma


print(zad(2, 3))
