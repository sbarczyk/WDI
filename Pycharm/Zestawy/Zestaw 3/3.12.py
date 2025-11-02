from random import randint

N = int(input("Podaj długość tablicy N: "))

def random_odd():
    odd = randint(1, 99) * 2 + 1
    return odd

def wypelnianie_tab(N):
    tab = [random_odd() for _ in range(N)]
    return tab

def zad12():
    tab = wypelnianie_tab(N)
    print(tab)

    if len(tab) <= 2:
        return "Wprowadź większą wartość N."

    max_leng_with_pos_r = 0
    max_leng_with_neg_r = 0
    counter = 2
    r = tab[1] - tab[0]

    for i in range(2, len(tab)):
        if r != 0:
            if tab[i] - tab[i - 1] == r:
                counter += 1
            else:
                if r > 0:
                    max_leng_with_pos_r = max(counter, max_leng_with_pos_r)
                elif r < 0:
                    max_leng_with_neg_r = max(counter, max_leng_with_neg_r)

                r = tab[i] - tab[i - 1]
                counter = 2

    if r != 0:
        if r > 0:
            max_leng_with_pos_r = max(counter, max_leng_with_pos_r)
        elif r < 0:
            max_leng_with_neg_r = max(counter, max_leng_with_neg_r)

    return max_leng_with_pos_r - max_leng_with_neg_r

print(zad12())
