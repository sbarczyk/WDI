from math import sqrt

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range (6, int(sqrt(x))+1, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True

def is_prime_digit(a):
    while a > 0:
        last_digit = a % 10
        if is_prime(last_digit):
            return True
        a //= 10
    return False

def check_line(line):
    for element in line:
        if not (is_prime_digit(element)):
            return False
    return True

def zad15(T):
    for line in T:
        if check_line(line):
            return True

    return False

tab = [ [24,12,13,926],
        [960,846,211,9],
        [666, 991, 484, 884],
        [645, 887, 666, 991] ]

print(zad15(tab))





