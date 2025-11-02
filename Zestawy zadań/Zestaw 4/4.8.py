def geometric_series(T):
    max_length = 0
    n = len(T)
    for x in range(n - 2):
        leng = 2
        q = T[1][x+1] / T[0][x]
        for i in range(2, n - x):
            if T[i][x+i] == T[i-1][x+i-1] * q:
                leng += 1
            else:
                max_length = max(max_length, leng)
                leng = 2
                q = T[i][x+i] / T[i-1][x+i-1]

        max_length = max(leng, max_length)

    for y in range(n-2):
        leng = 2
        q = T[y+1][1] / T[y][0]
        for i in range(n-y):
            if T[y+i][i] == T[y+i-1][i-1] * q:
                leng += 1
            else:
                max_length = max(leng, max_length)
                leng = 2
                q = T[y+i][i] == T[y+i-1][i-1]
        max_length = max(max_length, leng)

    return max_length if max_length >= 3 else False

T= [ [1,2,3,4],
     [5,6,7,8],
     [9,10,36,12],
     [13,14,15,216]]

print(geometric_series(T))

