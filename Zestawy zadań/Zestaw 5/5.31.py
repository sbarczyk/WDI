from math import sqrt


def dividers(n):
    divs = []
    i = 2
    while n != 1:
        if n % i == 0:
            divs.append(i)
            while n % i == 0:
                n //= i
        i += 1
    return divs


def zad31(n):
    divs = dividers(n)
    Sum = 0

    def rec(prod, i):
        nonlocal Sum
        if i == len(divs):
            Sum += prod
        else:
            rec(prod * divs[i], i + 1)
            rec(prod, i + 1)

    rec(1, 0)

    return Sum - 1


print(zad31(60))
print(dividers(60))
