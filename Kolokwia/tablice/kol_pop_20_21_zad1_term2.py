def wsp_czyn(a, b):
    cnt = 0

    i = 2
    while a != 1 and b != 1:
        cnt_a = 0
        while a % i == 0:
            a //= i
            cnt_a += 1

        cnt_b = 0
        while b % i == 0:
            b //= i
            cnt_b += 1

        cnt += min(cnt_a, cnt_b)
        i += 1

        if cnt > 1:
            return False

    return cnt == 1

def four(T):
    cnt = 0
    N = len(T)
    for y in range (1, N-1):
        for x in range(1, N-1):
            if wsp_czyn(T[y][x], T[y-1][x]) and wsp_czyn(T[y][x], T[y+1][x]) and \
            wsp_czyn(T[y][x], T[y][x+1]) and wsp_czyn(T[y][x], T[y][x-1]):
                cnt += 1
    return cnt
