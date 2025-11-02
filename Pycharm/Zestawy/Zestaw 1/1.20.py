from math import sqrt
EPS=1e-12

def zad20(A, B):
    while abs(A-B) > EPS:
        A, B = sqrt(A*B), (A+B)/2
    return A
print(zad20(1, 5))