def zad9(tab):
    counter = 1
    max_length = 0
    for i in range (1, len(tab)):
        if tab[i] > tab [i-1]:
            counter += 1
        else:
            max_length = max(counter, max_length)
            counter = 1

    return max_length

tab =[1,2,3,4,5,13,122, 134 ,0, 5, 4, 6, 8, 10]
print(zad9(tab))