def knight(T):
    n = len(T)
    min_steps = float("inf")
    moves = [(2,1), (2,-1), (1,2), (1, -2)]
    
    def rek(row, col, cnt):
        nonlocal min_steps
        
        if row == n-1:
            min_steps = min(min_steps, cnt)
            return
        
        for move in moves:
            if 0 <= row + move[0] < n and 0 <= col + move[1] < n:
                if not T[row + move[0]][col + move[1]]:
                    rek(row + move[0], col + move[1], cnt + 1)

    for i in range(n):
        if not T[0][i]:
            rek(0, i, 0)

    return min_steps if min_steps != float("inf") else "No path found"






