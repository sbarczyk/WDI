def next_a(a):
    a = 3 * a + 1
    return a

n = int(input())

def zad(n):
    a = 2
    while a <= n:
        a = next_a(a)
        print(a)
        if n % a == 0:
            return True
            break
    else:
        return False

print(zad(n))

