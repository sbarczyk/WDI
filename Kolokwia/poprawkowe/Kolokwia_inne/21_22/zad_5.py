

def czynnikowo_podobne(a, b):
    cnt = 0
    div  = 2
    while a != 1 and b != 1:
        cnt_a = 0
        while a % div == 0:
            cnt_a += 1
            a //= div

        cnt_b  =0
        while b % div == 0:
            cnt_b += 1
            b //= div

        div += 1
        cnt = min(cnt_a, cnt_b)
    
    return cnt == 1

print(czynnikowo_podobne(32,18))

def three(T):
    cnt = 0
    n = len(T)
    moves = [(-1,1),(-1,-1), (1,-1), (1,1)]
    
    for y in range(1, n-1):
        for x in range(1, n-1):
            curr = 0
            for move in moves:
                if czynnikowo_podobne(T[y][x], T[y+move[0]][x+move[1]]):
                    curr += 1

            if curr == 3:
                cnt += 1

    return cnt
