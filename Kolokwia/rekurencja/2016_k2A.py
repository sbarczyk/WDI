def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def zad(N):
    def rek(N, a, b, cnt_a, cnt_b):
        if N == 0:
            if nwd(a, b) == 1:
                return 1
            return 0

        return (
                rek(N // 10, a + ((N % 10) * (10 ** cnt_a)), b, cnt_a + 1, cnt_b) +
                rek(N // 10, a, b + ((N % 10) * (10 ** cnt_b)), cnt_a, cnt_b + 1)
        )
    return rek(N, 0, 0, 0, 0) // 2


print(zad(21523))
