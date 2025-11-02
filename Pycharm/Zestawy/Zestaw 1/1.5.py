def newton_rapson(num, eps = 1e-8):
    a, b = 1, num
    while abs(a - b) > eps:
        a = (a+b)/2
        b = num / a
    return a

print(newton_rapson(9))
