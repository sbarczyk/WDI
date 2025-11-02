def zad18(T):
    for e in T:
        print(e)

    n = len(T)

    biggest_sum = -float('inf')
    for r in range(n):
        for c in range(n):

            i = 0
            sum = 0
            while c + i < n and i < 10:
                sum += T[r][c + i]
                biggest_sum = max(biggest_sum, sum)
                i += 1

            i = 0
            sum = 0
            while r + i < n and i < 10:
                sum += T[r+i][c]
                biggest_sum = max(biggest_sum, sum)
                i += 1

    return biggest_sum

