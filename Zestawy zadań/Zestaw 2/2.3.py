def palindrom(x, base):
    starting_x = x
    counter = 0
    result = 0
    while x != 0:
        result += (x % base) * base**(counter)
        x //= base
        counter += 1
    return result == starting_x

x = int(input("Podaj liczbę: "))
base = int(input("Podaj system, w którym zapisana jest liczba: "))
print(palindrom(x, base))
