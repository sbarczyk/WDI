def krol(T, w, k):
    if w == 7:
        return T[w][k]

    if k > 0:
        left = krol(T, w + 1, k - 1)
    else:
        left = float('inf')

    if k < 7:
        right = krol(T, w + 1, k + 1)
    else:
        right = float(-inf)

    middle = krol(T, w + 1, k)

    return min(middle, left, right) + T[w][k]


print(krol(T, 0, k))
