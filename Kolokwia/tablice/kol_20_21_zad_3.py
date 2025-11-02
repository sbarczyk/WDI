def szachy(T):
    n = len(T)

    row = [0 for _ in range(n)]
    col = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            row[i] += T[i][j]
            col[i] += T[j][i]

    max_sum = 0
    x1 = y1 = x2 = y2 = None

    for w1 in range(n):
        for k1 in range(n):
            for w2 in range(n):
                for k2 in range(n):
                    if not (w1 == w1 and k1 == k2):
                        suma = row[w1] + col[k1] - 2 * (T[w1][k1] + T[w2][k2])
                        if w1 == w2:
                            suma += col[k2]
                            suma -= T[w2][k2]
                        elif k1 == k2:
                            suma += row[w2]
                            suma -= T[w2][k2]
                        else:
                            suma += (row[w2] + col[k2])
                            suma -= (T[w2][k1] + T[w1][k2])
                        if suma > max_sum:
                            max_sum = suma
                            x1 = w1
                            x2 = w2
                            y1 = k1
                            y2 = k2
    return (x1, y1), (x2, y2)


print(szachy([[1, 1, 2, 3], [-1, 3, -1, 4], [4, 1, 5, 4], [5, 0, 3, 6]]))
