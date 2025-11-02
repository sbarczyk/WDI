def is_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1


def rook_race(T):
    rook1_time = float('inf')
    rook2_time = float('inf')

    def rook1_rec(r=0, c=0, cnt=0):
        nonlocal rook1_time
        n = len(T)
        if r == c == n - 1:
            rook1_time = min(rook1_time, cnt)
        else:
            for i in range(r + 1, n):
                if is_coprime(T[r][c], T[i][c]):
                    rook1_rec(i, c, cnt + 1)
            for i in range(c + 1, n):
                if is_coprime(T[r][c], T[r][i]):
                    rook1_rec(r, i, cnt + 1)

    def rook2_rec(r=0, c=len(T) - 1, cnt=0):
        nonlocal rook2_time
        n = len(T)
        if r == n - 1 and c == 0:
            rook2_time = min(rook2_time, cnt)
        else:
            for i in range(r + 1, n):
                if is_coprime(T[r][c], T[i][c]):
                    rook2_rec(i, c, cnt + 1)
            for i in range(0, c):
                if is_coprime(T[r][c], T[r][i]):
                    rook2_rec(r, i, cnt + 1)

    rook1_rec()
    print(rook1_time)
    rook2_rec()
    print(rook2_time)
    if rook2_time == rook1_time:
        return 0
    elif rook1_time < rook2_time:
        return 1
    elif rook1_time > rook2_time:
        return 2


T = [
    [2, 0, 4],
    [3, 0, 0],
    [2, 0, 5]
]

print(rook_race(T))
