def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return a * b // nwd(a, b)

a = int(input('Wprowadź pierwszą liczbę: '))
b = int(input('Wprowadź druga liczbę: '))

gcd = nwd(a, b)
lcm = nww(a, b)

print("NWD:", gcd)
print("NWW:", lcm)
