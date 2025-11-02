# zmiana polecenia: "tak aby suma ELEMENTÓW podzbiorów wynosiła k"
def zad32(T, k):
    def rek(k, i, fir, fi, sec, si):
        if fi != 0 and fi == si and fir == sec == k:
            return True
        elif i == len(T):
            return False
        else:
            return rek(k, i + 1, fir, fi, sec, si) or rek(k, i + 1, fir + T[i], fi + 1, sec, si) or \
                rek(k, i + 1, fir, fi, sec + T[i], si + 1)

    return rek(k, 0, 0, 0, 0, 0)


print(zad32([2, 1, 3, 7, 0], 4))
