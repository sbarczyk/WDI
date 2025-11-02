def wzglednie_pierwsze(a, b):
    while b != 0:
        a, b = b, a%b
    return a == 1


def rook_race(T):
    left_rook_time = float('inf')
    right_rook_time = float('inf')
    n = len(T)
    
    def right_rook(r=0, c=0, cnt=0):
        nonlocal right_rook_time
        if r == c == n - 1:
            right_rook_time = min(right_rook_time, cnt)
        
        else:
            for new_r in range(r+1, n):
                if wzglednie_pierwsze(T[r][c], T[new_r][c]):
                    right_rook(new_r, c, cnt+1)
            for new_c in range(c+1, n):
                if wzglednie_pierwsze(T[r][c], T[r][new_c]):
                    right_rook(r, new_c, cnt + 1)

    def left_rook(r=0, c=n-1, cnt=0):
        nonlocal left_rook_time
        if r == n - 1 and c == 0:
            left_rook_time = min(left_rook_time, cnt)
        
        else:
            for new_r in range(r+1, n):
                if wzglednie_pierwsze(T[r][c], T[new_r][c]):
                    left_rook(new_r, c, cnt+1)
            for new_c in range(0, c):
                if wzglednie_pierwsze(T[r][c], T[r][new_c]):
                    left_rook(r, new_c, cnt + 1)

    right_rook()
    print(right_rook_time)
    left_rook()
    print(left_rook_time)


    if right_rook_time < left_rook_time:
        return 1
    elif right_rook_time > left_rook_time:
        return 2
    else:
        return 0
    
T = [
    [2, 0, 4],
    [3, 0, 0],
    [2, 0, 5]
]

print(rook_race(T))
            
    