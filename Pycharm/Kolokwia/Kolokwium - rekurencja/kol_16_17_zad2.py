T = [2, 3, 5, 7, 11, 13, 16]


def liczba_jedynek(x):
    cnt = 0
    while x > 0:
        cnt += x % 2
        x //= 2
    return cnt


def zad(T):
    def rek(i, a, b, c):
        n = len(T)
        if i == n:
            if a == b == c != 0:
                return True
            else:
                return False

        return rek(i + 1, a + liczba_jedynek(T[i]), b, c) or \
            rek(i + 1, a, b + liczba_jedynek(T[i]), c) or \
            rek(i + 1, a, b, c + liczba_jedynek(T[i]))

    return rek(0, 0, 0, 0)


print(zad(T))
