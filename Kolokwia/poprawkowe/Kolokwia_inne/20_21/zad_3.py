
def chess(T):
    n = len(T)
    maks = 0
    best = (None, None, None, None)

    row = [0 for _ in range(n)]
    col = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            row[i] += T[i][j]
            col[j] += T[i][j]
    
    for row1 in range(n):
        for col1 in range(n):
            for row2 in range(n):
                for col2 in range(n):
                    current_sum = 0
                    if not (row1 == row2 and col1==col2):
                        if row1 == row2:
                            current_sum += col[col1] + col[col2] - 2*(T[row1][col1] + T[row2][col2]) + row[row1]

                        elif col1 == col2:
                            current_sum += row[row1] + row[row2] - 2*(T[row1][col1] + T[row2][col2]) + col[col1]

                        else:
                            current_sum += row[row1] + row[row2] - 2*(T[row1][col1] + T[row2][col2]) - T[row1][col2] - T[row2][col1] + col[col1] + col[col2]

                    if current_sum > maks:
                        maks = current_sum
                        best = (row1, col1, row2, col2)

    return maks, best


print(chess([[4,0,2],[3,0,0],[6,5,3]]))
print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]]))
