def check(h1, h2):
    if h1[0] == h2[0]:  # poziom
        return True
    if h1[1] == h2[1]:  # pion
        return True
    if h1[0] - h1[1] == h2[0] - h2[1]:  # skos 1
        return True
    if h1[0] + h1[1] == h2[0] + h2[1]:  # skos 2
        return True
    return False


def hetmany(N):
    H = [None] * N
    cnt = 0

    def rek(row):
        nonlocal cnt
        if row == N:
            cnt += 1
            return

        for column in range(N):
            flag = False
            for queen in H[:row]:
                if check(queen, (row, column)):
                    flag = True
                    break

            if not flag:
                H[row] = (row, column)
                rek(row+1)
                H[row] = None
    rek(0)
    return cnt


print(hetmany(10))





