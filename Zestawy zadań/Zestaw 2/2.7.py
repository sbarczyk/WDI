from math import sqrt
def ciag(n):
    for i in range (1, int(sqrt(n))):
        A = i ** i + i + 1
        if n % A == 0:
            return True
    return False

n = int(input())

print(ciag(n))