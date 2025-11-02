def zad13(n):
    T = [0] * n

    def rek(n, i, T):
        if n == 0:
            print(T)
        if i == 0:
            mini = 1
        else:
            mini = T[i - 1]
        for j in range(mini, n + 1):
            T[i] = j
            rek(n - j, i + 1, T)
            T[i] = 0

    rek(n, 0, T)


print(zad13(3))
