T = [1, 3, 4, 2, 6, 7, 14, 1]


def zad(n, T, target):
    cnt = 0

    def rek(i, en, iloczyn):
        nonlocal cnt
        if iloczyn == target and en == n:
            cnt += 1
            return
        if i >= len(T):
            return
        if iloczyn > target or en > n:
            return
        rek(i + 1, en + 1, iloczyn * T[i])
        rek(i + 1, en, iloczyn)

    rek(0, 0, 1)
    return cnt


print(zad(3, T, 12))
