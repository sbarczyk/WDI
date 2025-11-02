from math import floor, log10

seq = [''] * 7


def get_leng(x):
    return floor(log10(x)) + 1


def A(x):
    if get_leng(x) < 2:
        return x
    else:
        y = x // 100
        d1 = (x % 100) // 10
        d2 = x % 10
        return y * 100 + d1 * 10 + d2


def B(x):
    return x * 3


def C(x):
    length = get_leng(x)

    if length >= 2:
        new_x = x % (10 ** (length - 1))
        return new_x
    else:
        return x


def rek(x, y, seq, i):
    if x == y:
        return seq
    if i >= 7:
        return []

    seq[i] = 'A'
    res = rek(A(x), y, seq, i + 1)
    if res:
        return res

    seq[i] = 'B'
    res = rek(B(x), y, seq, i + 1)
    if res:
        return res

    seq[i] = 'C'
    res = rek(C(x), y, seq, i + 1)
    if res:
        return res

    seq[i] = ''
    return []


result = rek(6, 3, seq, 0)
print(result)
