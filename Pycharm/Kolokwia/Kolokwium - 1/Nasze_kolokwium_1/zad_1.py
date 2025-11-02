T = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45]


def czy_zgodne(a, b):
    T = [None] * 1000
    i = 2
    while a != 1:
        if a % i == 0:
            T[i] = True
            while a % i == 0:
                a //= i
        i += 1

    i = 2
    while b != 1:
        if b % i == 0:
            if not T[i]:
                return False
            else:
                T[i] = False
            while b % i == 0:
                b //= i
        i += 1

    for element in T:
        if element:
            return False
    return True


def zgodne(T):
    tab = [False] * 1000
    counter = 0
    n = len(T)
    for i in range(n - 2):
        for j in range(i + 1, i + 3):
            if czy_zgodne(T[i], T[j]):
                tab[i] = True
                tab[j] = True

    for element in tab:
        if element:
            counter += 1
    return counter


print(zgodne(T))
