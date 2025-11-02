from math import sqrt

tab = [12, 8, 8, 16, 3, 6]

def is_in_fibo(x):
    a1, a2 = 0, 1
    while a1 <= x:
        if x == a1:
            return True
        a1, a2 = a2, a1 + a2
    return False

def is_prime(x):

    if x == 2 or x == 3:
        return True

    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False

    for i in range(6, int(sqrt(x)) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True
def is_composite(x):
    if not is_prime(x) and x >= 2:
        return True
    else:
        return False

def fib_num_comp(tab):
    for i, num in enumerate(tab):
        if is_in_fibo(i):
            if is_composite(num):
                pass
            else:
                return False
    return True

def one_prime_in_non_fib(tab):
    for i, num in enumerate(tab):
        if not is_in_fibo(i):
            if is_prime(num):
                return True
    return False

def zad(tab):
    if fib_num_comp(tab) and one_prime_in_non_fib(tab):
        return True
    else:
        return False

print(zad(tab))
