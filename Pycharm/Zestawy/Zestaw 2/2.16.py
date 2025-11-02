from math import sqrt

def sum_of_digits(x):
    sum = 0
    while x > 0:
        last_digit = x % 10
        x //= 10
        sum += last_digit
    return sum

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num <= 1 or num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(6, int(sqrt(num)) + 1, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
    return True
def sum_of_prime_fact(n):
    suma = 0
    i = 2
    while n != 1:
        while n % i == 0:
            suma += sum_of_digits(i)
            n //= i
        i += 1
    return suma

def is_smith(n):
    if sum_of_prime_fact(n) == sum_of_digits(n) and not is_prime(n):
        return True

def zad():
    for i in range (1, 1000):
        if is_smith(i):
            print(i)

zad()



