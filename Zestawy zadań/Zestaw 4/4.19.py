def zad19(T,x):
    n = len(T)
    moves = [(2,1),(2,-1),(1,-2),(-1,-2)]
    counter = 0
    for r in range(n):
        for c in range(n):
            for move in moves:
                if 0 <= r + move[1] < n and 0 <= c+move[0] < n and T[r][c] * T[r+move[1]][c+move[0]] == x:
                    counter += 1
    return counter


T = [
    [1,0,0,0],
    [1,0,1,0],
    [0,0,0,0],
    [0,1,0,0]
]

print(zad19(T,1))