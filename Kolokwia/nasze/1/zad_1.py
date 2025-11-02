def czy_jedno_zgodne(a, b):
    div = 2
    while a != 1 and b != 1:
        if a % div == 0:
            while a % div == 0:
                a //= div
            while b % div == 0:
                b //= div
        div += 1
    return a == 1 and b == 1



def zgodne(T):
    counter = 0
    for i in range(len(T)):
        for j in range(i-2, i+3):
            if 0 <= j < len(T) and j != i:
                if czy_jedno_zgodne(T[i], T[j]):
                    counter += 1
                    break
    return counter


𝑇 = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45]
print(zgodne(T))

