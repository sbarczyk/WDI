masa_do_odwazenia = 11
T = [10, 5, 4]


def zad9(T, masa_do_odwazenia):
    n = len(T)

    def rek(i, masa_szalki_1, masa_szalki_2, wybrane_odwazniki):
        if masa_szalki_1 == masa_szalki_2:
            return True, wybrane_odwazniki
        elif i == n:
            return masa_szalki_1 == masa_szalki_2

        return rek(i + 1, masa_szalki_1, masa_szalki_2, wybrane_odwazniki) or \
            rek(i + 1, masa_szalki_1 + T[i], masa_szalki_2, wybrane_odwazniki + [T[i]]) or \
            rek(i + 1, masa_szalki_1, masa_szalki_2 + T[i], wybrane_odwazniki + [T[i]])

    return rek(0, 0, masa_do_odwazenia, [])


print(zad9(T, 11))
