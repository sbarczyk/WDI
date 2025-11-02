def liczba_jedynek(x):
    cnt = 0
    while x > 0:
        cnt += x % 2
        x //= 2
    return cnt


def zad(N):
    def rek(i, a, b, c):
        if i == len(N):
            return a == b == c

        return rek(i + 1, a + liczba_jedynek(N[i]), b, c) or rek(i + 1, a, b + liczba_jedynek(N[i]), c) or \
            rek(i + 1, a, b, c + liczba_jedynek(N[i]))

    return rek(0, 0, 0, 0)


N = [5, 7, 15]
print(zad(N))
