
def right_row_rotate(T, row):
    n = len(T[row])
    new_matrix = [row[:] for row in T]
    tmp = new_matrix[row][n-1]
    
    for i in range(n-1, 0, -1):
        new_matrix[row][i] = new_matrix[row][i-1]
    new_matrix[row][0] = tmp
    return new_matrix

def down_col_rotate(T, col):
    n = len(T)
    new_matrix = [row[:] for row in T]
    
    tmp = new_matrix[n-1][col]
    
    for i in range(n-1, 0, -1):
        new_matrix[i][col] = new_matrix[i-1][col]
    new_matrix[0][col] = tmp
    return new_matrix

def check(T):
    row_sum = 0
    col_sum = 0
    
    for i in range(len(T)):
        row_sum += T[0][i]
        col_sum += T[i][0]

    for j in range(1, len(T)):
        curr_row = 0
        curr_col = 0
        for k in range(len(T)):
            curr_row += T[j][k]
            curr_col += T[k][j]
        
        if curr_row != row_sum or curr_col != col_sum:
            return False
    
    return True

def magic(T, n = 2):
    if n == 0:
        return check(T)
    
    for i in range(len(T)):
        if magic(right_row_rotate(T, i), n - 1) or magic(down_col_rotate(T, i), n-1):
            return True
    return False


T = [
    [3,11,14,17],
    [6,12,7,9],
    [10,8,16,13],
    [5,15,4,2]
]
print(magic(T))

