def inter(A, B):
    if A[0] <= B[0] <= A[1] or A[2] <= B[2] <= A[3] or A[0] <= B[1] <= A[1] or A[2] <= B[3] <= A[3]:
        return True
    else:
        return False




def zad27(T):
    n = len(T)
    Taken = [False for _ in range(n)]

    def rek(i, cnt, area):
        if i == n and cnt == 3 and area == 6:
            return True
        if i > n or cnt > 3 or area > 6:
            return False

        valid_candidate = True
        if i < n:
            for k in range(i):
                if Taken[k] and inter(T[k], T[i]):
                    valid_candidate = False
                    break

            if valid_candidate:
                Taken[i] = True
                if rek(i + 1, cnt + 1, area + ((T[i][1] - T[i][0]) ** 2)):
                    return True
                Taken[i] = False
        return rek(i + 1, cnt, area)

    return rek(0, 0, 0)


T = [(12, 2, 1, 2), (1, 3, 1, 3), (4, 5, 4, 5), (7, 8, 7, 8)]
print(zad27(T))
