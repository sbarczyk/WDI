


def king(N,L):

    def rek(cnt, prev, w, k):
        if (w, k) == (N-1, N-1):
            return cnt
        longest_path = 0
        if w > 0 and w-1 != prev and not (w-1, k) in L:
            longest_path = max(rek(cnt+1, w, w-1, k), longest_path)
        if w + 1 < N and w+1 != prev and not (w+1, k) in L:
            longest_path = max(rek(cnt + 1, w, w + 1, k), longest_path)
        if k + 1 < N and k+1 != prev and not (w, k+1) in L:
            longest_path = max(rek(cnt+1, k, w, k+1), longest_path)

        if longest_path == 0:
            return 0

        return longest_path

    ans = rek(0, -1, 0, 0)
    return None if ans == 0 else ans


L = []
print(king(8, L))



