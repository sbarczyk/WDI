from math import log, floor

def get_length(x):
    return (floor(log(x, 10)) + 1)

def zad(x):
    contains = False
    length = get_length(x)
    while x > 0:
        p = x % 10
        x //= 10
        if p == length:
            contains = True

    if contains:
        print("Zawiera cyfrę równą liczbie swoich cyfr.")
    else:
        print("Nie zawiera")

zad(1333)