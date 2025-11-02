num=int(input("Wprowadź liczbę:"))
base=int(input("System: "))
def przelicz_na_system(num, base):
    result = ''

    while num!=0:
        next_digit = num%base
        num //= base
        if next_digit>=10:
            next_digit -= 10
            result = chr(ord('A')+next_digit) + result
        else:
            result = str(next_digit) + result
    return result
print(przelicz_na_system(num, base))

