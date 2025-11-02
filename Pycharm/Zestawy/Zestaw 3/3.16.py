tab = [1,2,3,5,7,8,9,]

def zad(tab):
    maxi = tab[0]
    mini = tab[0]
    flag_maxi = 0
    flag_mini = 0

    for i in range(1, len(tab)):
        if tab[i] < mini:
            mini = tab[i]
        if tab[i] > maxi:
            maxi = tab[i]

    for i in range (len(tab)):
        if tab[i] == mini:
            flag_mini += 1
        if tab[i] == maxi:
            flag_maxi += 1


    if flag_mini == 1 and flag_maxi == 1:
        return True
    else:
        return False

print(zad(tab))

