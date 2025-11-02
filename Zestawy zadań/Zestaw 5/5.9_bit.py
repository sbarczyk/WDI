T = [5, 4, 10]


def f(T, i, r, w1=[], w2=[]):
    n = len(T)

    if r == 0:
        print(w1, w2)
        return True

    if r < 0 or i > n - 1:
        return False

    return f(T, i + 1, r, w1, w2) or f(T, i + 1, r - T[i], w1 + [T[i]], w2) or f(T, i + 1, r + T[i], w1, w2 + [T[i]])


print(f(T, 0, 11))
