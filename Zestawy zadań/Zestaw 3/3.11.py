def zad11(tab):
    if len(tab) == 0: return 0
    if len(tab) == 1: return 1
    counter = 2
    max_length = 2
    q = round(tab[1]/tab[0], 5)

    for i in range(2, len(tab)):
        if tab[i] / tab[i - 1] == q:
            counter += 1
        else:
            max_length = max(counter, max_length)
            counter = 2
            q = round(tab[i] / tab[i - 1], 5)

    max_length = max(counter, max_length)
    return max_length

tab = [1,2,4,8,16,32,64,128,0]
print(zad11(tab))