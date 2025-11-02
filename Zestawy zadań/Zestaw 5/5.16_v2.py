def liczba_samoglosek(s):
    cnt = 0
    samogloski = ['a', 'o', 'u', 'i', 'y', 'e']
    for i in range(len(s)):
        if s[i] in samogloski:
            cnt += 1
    return cnt


def suma_ascii(s):
    suma = 0
    for i in range(len(s)):
        suma += ord(s[i])
    return suma


def czy_waga(s1, s2):
    if liczba_samoglosek(s1) == liczba_samoglosek(s2):
        return suma_ascii(s1) == suma_ascii(s2)


def wyraz(s1, s2):
    def rek(i, res):
        if i == len(s2):
            return czy_waga(s1, res)

        if rek(i + 1, res + s2[i]) or rek(i+1, res):
            return True
        return False

    return rek(0, '')


print(wyraz('ula', 'luka'))
