def zad(T):
    n = len(T)

    def rek(i, cnt):
        if i == n - 1:
            return cnt

        if i >= n:
            return float('inf')

        if T[i] == 0 and i < n - 1:
            return float('inf')

        best_path = float('inf')
        div = 2

        while T[i] != 1:
            if T[i] % div == 0 and div < T[i]:
                best_path = min(rek(i + div, cnt + 1), best_path)

            while T[i] % div == 0:
                T[i] //= div

            div += 1

        return best_path if best_path != float('inf') else -1
    return rek(0, 0)


T = [14, 8, 6, 8, 9]
print(zad(T))
