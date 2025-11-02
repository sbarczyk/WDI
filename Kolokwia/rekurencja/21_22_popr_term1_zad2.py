T = [(1, 2020), (3, 2026), (2021, 2022), (2024, 2028)]


def inter(A, B):
    return (B[0] <= A[0] <= B[1]) or (B[0] <= A[1] <= B[1])


def odcinki(T):
    n = len(T)
    U = [False] * n

    def rek(i, suma):
        if i == n:
            return suma == 2022

        valid_candidate = True
        for x in range(i-1):
            if inter(T[i], T[x]):
                valid_candidate = False
                break

        if valid_candidate:
            if rek(i + 1, suma + T[i][1] - T[i][0]):
                return True
            U[i] = False
        return rek(i + 1, suma)

    return rek(0, 0)


print(odcinki(T))
