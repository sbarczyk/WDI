def f(x):
    return x*x - 2020

def solve(eps=1e-8):
    a,b = 0, 100
    while abs(a-b) > eps:
        x = (a+b) / 2
        if f(x) == 0:
            return x
        if f(a)*f(x) < 0:
            b = x
        if f(x) * f(b) < 0:
            a = x

    return (a+b)/2

print(solve())
