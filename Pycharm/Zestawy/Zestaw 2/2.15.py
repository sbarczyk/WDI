from math import log10, floor
N = int(input("Wprowadź N: "))
def get_length(x):
    return (floor(log10(x)) + 1)

def check(x):
    starting_x = x
    length = get_length(x)
    result = 0
    while x > 0:
        last_digit = x % 10
        result += last_digit ** length
        x //= 10
    if result == starting_x:
        return True
    else:
        return False

def zad(N):
    for i in range (1, N+1):
        if check(i):
            print(i)
    exit(0)

print(zad(N))



