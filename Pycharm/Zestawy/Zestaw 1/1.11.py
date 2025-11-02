from math import sqrt
a = int(input("Wprowadź pierwszą liczbę: "))
b = int(input("Wprowadź drugą liczbę: "))

def sum_of_div(num):
    sum = 1
    for i in range (2, int(sqrt(num))+1):
        if num % i == 0:
            if num == i ** i:
                sum += i
            else:
                sum += (i+(num//i))
    return sum

def zad11(a, b):
    if sum_of_div(a) == b and sum_of_div(b) == a:
        print("Liczby są zaprzyjaźnione")
    else:
        print("Liczby NIE są zaprzyjaźnione")

zad11(a, b)