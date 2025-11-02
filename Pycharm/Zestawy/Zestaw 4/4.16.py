from math import isqrt

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x)+1, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True

def is_digit_only_prime(x):
    while x > 0:
        last_digit = x % 10
        x //= 10
        if not is_prime(last_digit):
            return False
    return True

def check_line(line):
    for element in line:
        if is_digit_only_prime(element):
            return True
    return False

def zad16(T):
    for line in T:
        if not check_line(line):
            return False
    return True

tab = [ [1,11,33,460],
        [614,583,22,913],
        [918,332,232,59183],
        [5981,322,33354,5913]]

print(zad16(tab))

