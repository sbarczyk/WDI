def is_last_unique(x):
    last_digit = x % 10
    x //= 10
    while x > 0:
        if x % 10 == last_digit:
            return False
        x //= 10
    return True

print(is_last_unique(12322))