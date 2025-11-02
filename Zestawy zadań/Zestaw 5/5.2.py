def waga(x):
    counter = 0
    i = 2
    while x != 1:
        if x % i == 0:
            counter += 1
        while x % i == 0:
            x //= i
        i += 1
    return counter


def zad2(T):
    n = len(T)

    def rek(i, a, b, c):
        if i == n:
            return a == b == c

        return rek(i + 1, a + waga(T[i]), b, c) or rek(i + 1, a, b + waga(T[i]), c) or rek(i + 1, a, c + waga(T[i]))

    return rek(0, 0, 0, 0)
