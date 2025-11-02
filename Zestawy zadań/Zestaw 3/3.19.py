def zad19(T):
    n = len(T)
    maxi = 0
    for i in range(n - 1):
        suma = T[i]
        cnt = 1
        sum_ind = i
        if T[i] < T[i+1]:
            for j in range(i + 1, n):
                if T[j-1] >= T[j]:
                    break
                else:
                    suma += T[j]
                    sum_ind += j
                    cnt += 1

                    if suma == sum_ind:
                        maxi = max(maxi, cnt)
    return maxi

T = [1, 2, 1, 3, 5, 6, 7, 7, 8, 9, 13, 4]
print(zad19(T))

