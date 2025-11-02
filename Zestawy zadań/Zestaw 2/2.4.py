N = int(input("Podaj zakres N: "))
def is_235(n):
    for x in (2, 3, 5):
        while n % x == 0:
            n //= x
    if n == 1:
        return True
    else:
        return False

def zad(N):
    sum = 2
    for i in range (3, N+1):
        if is_235(i):
            sum += 1
            print(i)
    return sum
result = zad(N)
print ("Liczb dwu-trzy-piątkowych jest: ", result)
