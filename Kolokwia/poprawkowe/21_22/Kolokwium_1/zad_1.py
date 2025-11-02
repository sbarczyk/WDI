def is_on_board(y, x, N):
    return 0 <= y < N and 0 <= x < N

def how_many_free(T, N):
    tab = [[False] * N for _ in range(N)]
    moves = [(0, 0), (-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
    cnt = 0

    for knight in T:
        for move in moves:
            if is_on_board(knight[0] + move[0], knight[1] + move[1], N):
                tab[knight[0] + move[0]][knight[1] + move[1]] = True

    for y in range(N):
        for x in range(N):
            if not tab[y][x]:
                cnt += 1
    return cnt

def usun(T, N):
    before = how_many_free(T, N)
    best = 0

    for i in range(len(T)):
        T_without_knight_i = T[:i] + T[i+1:]
        best = max(best, how_many_free(T_without_knight_i, N))

    return best - before

T = [(1, 1), (2, 3), (4, 1), (4, 5)]
print(usun(T, 8))
