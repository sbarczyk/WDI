num = int(input("Wprowadź liczbę: "))
system = int(input("Podaj system liczbowy: "))

def zamiana(num, system):
    result = ''

    while num != 0:
        next_digit = num % system
        num //= system
        if next_digit > 10:
            next_digit -= 10
            result = chr(ord("A") + next_digit) + result

        else:
            result = result + str(next_digit)

    return result

print(zamiana(num, system))