def nachodzenie(A, B):
    return B[0] <= A[0] <= B[1] or B[0] <= A[1] <= B[1]


def zad(T):
    def rek(i, suma, P, cnt):
        if suma == 2022:
            return True
        if suma > 2022:
            return False
        if i == len(T):
            return False

        for k in range(cnt):
            if nachodzenie(T[i], T[P[k]]):
                break
        else:
            if rek(i+1, suma, P, cnt):
                return True
            P[cnt] = i
            return rek(i + 1, suma + (T[i][1] - T[i][0]), P, cnt + 1)

        return rek(i + 1, suma, P, cnt)

    P = [0] * len(T)
    return rek(0, 0, P, 0)


T = [(1, 2020), (3, 2026), (2021, 2024), (2024, 2028)]
print(zad(T))
