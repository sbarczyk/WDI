a = int(input())
b = int(input())
n = int(input())

def zad(a, b, n):

    print(a//b, "." if a%b != 0  else "", sep = "", end = "" )
    a %= b
    while a >0 and n > 0:
        a *= 10
        print(a//b, end="")
        a %= b
        n -= 1

zad(a, b, n)