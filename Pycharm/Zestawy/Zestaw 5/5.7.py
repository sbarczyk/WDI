masa = 11
T = [5, 5, 1]


def zad7(T, masa):
    n = len(T)

    def rek(i, masa_odwaznikow):
        if masa_odwaznikow == masa:
            return True
        elif i == n:
            return masa_odwaznikow == masa

        return rek(i + 1, masa_odwaznikow) or rek(i + 1, masa_odwaznikow + T[i])

    return rek(0, 0)

print(zad7(T, masa))
