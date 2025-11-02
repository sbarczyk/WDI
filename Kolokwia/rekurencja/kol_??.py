def skoczek(T):
    def rek(w, k, cnt):
        if k < 0 or k >= len(T) or w >= len(T):
            return float('inf')

        if not T[w][k]:
            return float('inf')

        if w == (len(T) - 1):
            return cnt

        return min(rek(w + 1, k - 2, cnt + 1), rek(w + 1, k + 2, cnt + 1), rek(w + 2, k - 1, cnt + 1),
                   rek(w + 2, k + 1, cnt + 1))

    ans = float('inf')
    for i in range(len(T)):
        return min(ans, rek(0, i, 0))

    return ans
