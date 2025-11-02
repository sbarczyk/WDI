def czy_4_zgodne(a, b):
    T = [0] * 4
    while a > 0:
        if T[a % 4] == 0:
            T[a % 4] = 1
        a //= 4

    while b > 0:
        if T[b % 4] == 1:
            T[b % 4] = 2
        elif T[b % 4] == 0:
            return False
        b //= 4

    for element in T:
        if element == 1:
            return False
    return True


def zad(T):
    max_length = 1
    for i in range(len(T) - 1):
        leng = 1
        for j in range(i + 1, len(T)):
            if czy_4_zgodne(T[i], T[j]):
                leng += 1
                print((T[i], T[j]))
        max_length = max(max_length, leng)
    max_length = max(max_length, leng)
    return max_length


T = [13, 13, 1367, 2, 13, 13, 13]
wynik = zad(T)
print(wynik)
