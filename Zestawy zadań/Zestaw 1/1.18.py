
def newton_raphson3(num):
    eps = 1e-8
    a = num
    x = 1

    while abs(a-x) > eps:
        x = (2*x+a)/3
        a = num/x/x
    return x

print(newton_raphson3(27))