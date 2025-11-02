def liczba_jedynek(n):
    cnt = 0
    while n != 0:
        cnt += n % 2
        n //= 2
    return cnt


def rek(T, i, a, b, c):
    if i == len(T):
        if a == b == c:
            return True
        else:
            return False

    return (
            rek(T, i + 1, a + liczba_jedynek(T[i]), b, c) or
            rek(T, i + 1, a, b + liczba_jedynek(T[i]), c) or
            rek(T, i + 1, a, b, c + liczba_jedynek(T[i]))
    )


T = [2, 3, 5, 7, 11, 13, 16]
print(rek(T, 0, 0, 0, 0))
