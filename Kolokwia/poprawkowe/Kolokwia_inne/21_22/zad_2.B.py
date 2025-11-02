from math import log10, floor, isqrt

def rotate(n):
    leng = floor(log10(n)) + 1
    first_digit = n // 10**(leng-1)
    n = n % (10 **(leng-1))
    n *= 10
    n += first_digit
    return n

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x)+1, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True

def zad(n):
    leng = int(log10(n)) + 1
    for base in range(2, 17):
        for _ in range(leng):
            n_copy = rotate(n)
            iloczyn = 1
            while n_copy > 0:
                if n_copy % base < 10:
                    iloczyn *= n_copy % base
                n_copy //= base
            if is_prime(iloczyn):
                return base
    return None

print(zad(16))