from random import randint
n = int(input('Wprowadź n: '))
tab = [randint(1,1000) for _ in range (n)]
print(tab)
def is_odd_el(x):
    while x > 0:
        if ((x % 10) % 2) == 1:
            return True
        x //= 10
    return False

def zad():
    for element in tab:
        if is_odd_el(element):
            pass
        else:
            print("NIE")
            exit(0)
    return ("TAK")

print(zad())


