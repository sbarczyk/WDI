from random import randint

tab = [[1, -1, 3, -3],
       [5, 5, 5, 5],
       [2, 2, 1, 2],
       [42, 24, 71, 56]]
def sumowanie_wierszy(tab):
    suma = 0
    n = len(tab)
    suma_wierszy = [0 for _ in range(n)]

    for i in range(n):
        suma = 0
        for j in range(n):
            suma += tab[i][j]
        suma_wierszy[i] = suma

    return suma_wierszy


def sumowanie_kolumn(tab):
    suma = 0
    n = len(tab)
    suma_kolumn = [0 for _ in range(n)]

    for i in range(n):
        suma = 0
        for j in range(n):
            suma += tab[j][i]
        suma_kolumn[i] = suma

    return suma_kolumn


def ratio_check_in_tab(tab):
    suma_wierszy = sumowanie_wierszy(tab)
    suma_kolumn = sumowanie_kolumn(tab)
    ratio = max = 0
    score = [0,0,0]
    n = len(tab)

    for i in range(n):
        for j in range(n):
            if suma_wierszy[i] != 0:
                ratio = suma_kolumn[j] / suma_wierszy[i]
                if ratio > max:
                    max = ratio
                    score[0], score[1], score[2] = ratio, i, j
    return score

def print_tab(tab):
    for line in tab:
        print(line)
    print("------------")

print_tab(tab)
print(ratio_check_in_tab(tab))