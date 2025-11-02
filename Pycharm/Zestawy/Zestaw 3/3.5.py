tab = [0] * 10

def zad5():
    while True:
        x= int(input())
        if x == 0:
            break
        insert(x, tab)
    print(tab[0])



def insert(n, tab):
    for i in range (1,11):
        if n > tab[-i]:
            n, tab[-i] = tab[-i], n

zad5()