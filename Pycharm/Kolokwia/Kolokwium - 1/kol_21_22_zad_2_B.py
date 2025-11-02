from math import log10, floor, isqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True


def get_length(x):
    return floor(log10(x)) + 1


def rotate(x):
    length = get_length(x)
    other_digits = x % (10 ** (length - 1))
    first_digit = x // (10 ** (length - 1))
    new_num = other_digits * 10 + first_digit
    return new_num


def zad(x):
    length = get_length(x)
    new_x = 0
    for base in range(2, 17):
        for _ in range(length):
            x = rotate(x)
            copy_x = x
            has_prime = False
            while copy_x > 0:
                digit = copy_x % base
                copy_x //= base
                if digit != 1 and digit < 10:
                    if is_prime(digit) and not has_prime:
                        has_prime = True
                    else:
                        break
            else:
                return base
        return None


