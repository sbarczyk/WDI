def check_if_diff_digits(a, b, system):

    digits = [False for _ in range (system)]

    while a > 0:
        digits [a % system] = True
        a //= system

    while b > 0:
        if digits [b % system]:
            return False
        b //= system
    return True

def zad(a, b):
    for system in range (2, 17):
        if check_if_diff_digits(a, b, system):
            return system
    return ("Podstawa systemu nie istnieje")

print(zad(123, 522))