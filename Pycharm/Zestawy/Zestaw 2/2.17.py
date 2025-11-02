from math import log, e

def f(x):
    return x**x - 2020

def f_prim(x):
    return (x ** x) * (log(x,e)+1)

def Newton(x, eps=10e-2):
    while abs(f(x)) > eps:
        x = x - f(x)/f_prim(x)
    return x, f(x)

print(Newton(4))