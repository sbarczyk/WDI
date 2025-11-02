def check(a, b):
    digits = [0 for _ in range (10)]
    while a > 0:
        digits [a % 10] += 1
        a //= 10

    while b > 0:
        digits [b % 10] -= 1
        b //= 10

    for element in digits:
        if element != 0:
            return False
    return True

print(check(123,325))
