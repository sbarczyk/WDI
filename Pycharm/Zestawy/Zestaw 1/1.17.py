def golden_ratio(a, b):
    eps = 1e-4
    while abs(b/a - (a+b)/b) > eps:
        a, b = b, a+b

    return (b/a)

print(golden_ratio(1,1))
