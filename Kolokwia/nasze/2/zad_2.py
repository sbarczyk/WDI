from math import floor, log10

def A(x):
    div = 2
    suma = 1
    while div ** 2 < x:
        if x % div == 0:
            suma += (div + x // div)
        div += 1

        if div ** 2 == x:
            suma += div
    
    return suma

def B(x):
    a, b  = 0, 1 
    while a <= x:
        a, b = b, a+b
    return a

def rewers(x):
    res = 0
    leng = floor(log10(x)) + 1
    while x > 0:
        res = res*10 + x % 10
        x //= 10
    return res

def C(x):
    return x + rewers(x)

def rek(a, b, n, cnt, res=[]):
    if a == b:
        print(res+[b])
        return cnt
    
    if n == 0:
        return None
    
    if r := rek(A(a), b, n - 1, cnt + 1, res + [a, 'A']):
        return r
    if r := rek(B(a), b, n - 1, cnt + 1, res + [a, 'B']):
        return r
    if r := rek(C(a), b, n - 1, cnt + 1, res + [a, 'C']):
        return r
    
def cycle(a, n):
    if r := rek(A(a), a, n - 1, 1, res=['A']):
        return r
    if r := rek(B(a), a, n - 1, 1, res=['B']):
        return r
    if r := rek(C(a), a, n - 1, 1, res=['C']):
        return r
    return -1

print(cycle(29, 6))