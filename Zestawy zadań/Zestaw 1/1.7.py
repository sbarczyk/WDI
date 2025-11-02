def zad7(number):
    a1, a2 = 1, 1
    while a1 * a2 <= number:
        if a1 * a2 == number:
            return True
        a1, a2 = a2, a1 + a2
    return False

number = int(input())
print(zad7(number))