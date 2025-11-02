EPS = 1e-12

def wyznacz_e():
    e = 2
    fact = 1
    i = 2

    while True:
        fact *= i
        i += 1
        next_elem = 1 / fact
        if next_elem < EPS:
            break
        e += next_elem

    return e
print(wyznacz_e())