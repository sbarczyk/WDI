def zad10(tab):
    if len(tab) == 0: return 0
    if len(tab) == 1: return 1

    counter = 2
    max_length = 2
    r = tab[1] - tab[0]

    for i in range (2, len(tab)):
        if tab[i] - tab[i-1] == r:
            counter += 1
        else:
            max_length = max(counter, max_length)
            counter = 2
            r = tab[i] - tab[i - 1]

    max_length = max(counter, max_length)

    return max_length

tab = [1,2,3,4,5,6,7,8,9, 10, 11]
print(zad10(tab))
