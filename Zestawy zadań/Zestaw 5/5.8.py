masa_do_odwazenia = 11
T = [10, 5, 2]


def zad7(T):
    n = len(T)

    def rek(i, masa_odwaznikow, masa_do_odwazenia):
        if masa_odwaznikow == masa_do_odwazenia:
            return True
        elif i == n:
            return False
        return rek(i + 1, masa_odwaznikow, masa_do_odwazenia) or \
            rek(i + 1, masa_odwaznikow + T[i], masa_do_odwazenia) or \
            rek(i + 1, masa_odwaznikow, masa_do_odwazenia + T[i])

    return rek(0, 0, masa_do_odwazenia)


print(zad7(T))
