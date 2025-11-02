def zad4(number):
    counter = 0
    while number >= 0:
        number -= counter * 2 + 1
        counter += 1
    return counter-1

number = int(input("Wprowadź liczbę: "))
print(zad4(number))



