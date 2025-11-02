from math import isqrt, log10, floor

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    
    for i in range(6, isqrt(x)+1, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True


def divide(N, parts=0):
    if N == 0:
        return(is_prime(parts))
    
    leng = floor(log10(N)) + 1

    for cut_leng in range(1, leng + 1):
        prefix = N // (10**(leng - cut_leng))
        new_n = N % (10**(leng - cut_leng))
        if is_prime(prefix):
            if divide(new_n, parts + 1):
                return True
    
    return False

print(divide(273))