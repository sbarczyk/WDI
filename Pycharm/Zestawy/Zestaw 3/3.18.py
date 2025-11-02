T = [1,3,5,7,7,5,3,1]
def is_odd(a):
    return a % 2 == 1

def palindrom(T, a, b):
    n = len(T)
    i = 0
    counter = 0
    while b + i < n and a - i >= 0:
        if not T[b+i] == T[a-i]:
            return counter
        if is_odd(T[b+i]) and is_odd(T[a-i]):
            counter += 2
            i += 1
        else:
            return counter
    return counter

def zad18(T):
    n = len(T)
    maxi = 0
    for i in range (1, n - 1):
        if is_odd(T[i]):
            if is_odd(T[i+1]) and T[i] == T[i + 1]:
                maxi = max(maxi, palindrom(T,i, i+1))
            maxi = max(maxi, palindrom(T, i-1, i+1) + 1)
    return maxi

print(zad18(T))