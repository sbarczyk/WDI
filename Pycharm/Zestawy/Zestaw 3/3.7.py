from random import randint
n = int(input('Wprowadź n: '))
tab = [randint(1,1000) for _ in range(n)]
print(tab)
def if_only_odd(x):
    while x > 0:
        if (x % 10) % 2 == 1:
            pass
        else:
            return False
        x //= 10
    return True

def zad(tab):
    for element in tab:
        if if_only_odd(element):
            print(element)
            return ("TAK")
    return ("NIE")

print(zad(tab))

