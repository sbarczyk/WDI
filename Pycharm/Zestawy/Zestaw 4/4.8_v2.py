def zad8(T):
    n = len(T)
    maxi = 0
    for i in range (n):
        for j in range(n):
            k = 0
            lengt = 2
            while i + k < n - 2 and j + k < n - 2:
                q = T[i+k][j+k] / T[i+k+1][j+k+1]
                if T[i+k+1][j+k+1] / T[i+k+2][j+k+2] == q:
                    lengt += 1
                    k += 1
                else:
                    break
            if lengt <= 3:
                maxi = max(maxi, lengt)
    return maxi if maxi != 0 else None
