def rook(N, L):
    def rek(w, k, cnt, T):
        if w == N - 1 and k == N - 1:
            print(T)
            return cnt
        if w >= N or k >= N:
            return float('inf')

        best_path = float('inf')

        for new_w in range(w + 1, N):
            if (new_w, k) in L:
                break
            best_path = min(rek(new_w, k, cnt + 1, T + [(new_w, k)]), best_path)

        for new_k in range(k + 1, N):
            if (w, new_k) in L:
                break
            best_path = min(rek(w, new_k, cnt + 1, T + [(w, new_k)]), best_path)

        return best_path

    return rek(0, 0, 0, [])


N = 3
L = [(0, 2), (1, 0)]
print(rook(N, L))
