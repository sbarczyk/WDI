def zad(T, k):
    def rek(w, k):
        if w == 7:
            return T[w][k]

        if k < 0:
            return float('inf')
        else:
            left = rek(w+1, k-1)

        if k >= len(T):
            return float('inf')
        else:
            right = rek(w+1, k+1)

        middle = rek(w+1, k)

        return min(left, middle, right) + T[w][k]

