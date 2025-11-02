def are_friends(a, b):
    T = [0 for _ in range (10)]

    while a > 0:
        last_digit = a % 10
        T[last_digit] = 1
        a //= 10

    while b > 0:
        last_digit = b % 10
        b //= 10
        if T[last_digit] != 0:
            T[last_digit] = 2
        else:
            return False

    for i in range(len(T)):
        if T[i] == 1:
            return False
    return True

def side(T, i, j):
    n = len(T)
    sides = [(-1,0),(-1,-1),(-1,1),(1,-1),(1,1),(1,0),(0,1),(0,-1)]
    for k in sides:
        if 0 <= i+k[0] < n and 0 <= j+k[1] < n:
            if not are_friends(T[i][j], T[i+k[0]][j+k[1]]):
                return False
    return True

def zad11(T):
    n = len(T)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if side(T,i,j):
                cnt += 1
    return cnt

T = [
     [2,2,2,4],
     [2,2,2,4],
     [2,2,2,4],
     [5,5,5,5]
     ]

print(zad11(T))

