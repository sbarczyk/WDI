def is_singleton(num, T):
    n = len(T)
    flag = False
    for i in range(n):
        for j in range(n):
            if (T[i][j]) == num and not flag:
                flag = True
            elif T[i][j] == num and flag:
                return False
    return True

def push(T, num, i):
    n = len(T)
    temp = T[i]
    T[i] = num
    for j in range(i, n-1):
        T[j+1], temp = temp, T[j+1]

def pseudosort(T, num):
    n = len(T)
    i = 0
    while T[i] < num:
        if T[i] == 0:
            T[i] = num
            return
        i += 1
    if i == n-1:
        T[i] = num
    else:
        push(T, num, i)

def zad6(T1):
    n = len(T1)
    T2 = [0 for _ in range (n*n)]
    for i in range (n):
        for j in range(n):
            if is_singleton(T1[i][j], T1):
                pseudosort(T2, T1[i][j])

    return T2

T1 = [[12,7,5], [5,8,6], [7,9,1]]

print(zad6(T1))






