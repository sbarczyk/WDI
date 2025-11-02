n = int(input())
tab = [0] * (n + 1)

def long_division(a, b, t):
    t[0] = a // b
    a = a % b
    for i in range(1, len(t)):
        a *= 10
        t[i] = a // b
        a = a % b
        if a == 0:
            return t

def zad4(n):
    digits = [1] + [0] * (n)
    fact = 1
    k = 1
    while fact < 10 ** n + 1:
        fact *= k
        k += 1
        long_division(1, fact, tab)
        for i in range(n+1):
            digits[i] += tab[i]

    for i in range(len(digits) - 1, 0, -1):
        digits[i - 1] += digits[i] // 10
        digits[i] %= 10
    return digits[:n+1]

print(zad4(n))
