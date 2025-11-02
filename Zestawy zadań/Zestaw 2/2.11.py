def czy_rosnacy(n):
    p = 10
    while n > 0:
        last = n % 10
        n //= 10
        if p <= last:
            return False
        p = last
    return True

print(czy_rosnacy(1976))