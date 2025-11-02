from math import sqrt
def is_in_fibb(num):
    if num == 1:
        return True
    a1, a2 = 1, 1
    while a1+a2 <= num:
        if a1 + a2 == num:
            return True
        a1, a2 = a2, a1+a2
    return False


def zad():
    a = int(input('Wprowadź liczbę: '))
    for i in range(1, int(sqrt(a)+1)):
        if a%i == 0:
            if is_in_fibb(i):
                if is_in_fibb(a//i):
                    print("Da się. Wprowadzona liczba jest iloczynem liczb: " + str(i) + " i " + str(a // i))
                    return True

    return False


print(zad())

