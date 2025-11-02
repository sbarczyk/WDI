def zad9(T, k):
    n = len(T)

    for bok in range(3,n,2):
        for y in range(n-bok+1):
            for x in range(n-bok+1):
                iloczyn = 1
                if y + bok - 1 < n and x + bok - 1 < n:
                    iloczyn = T[y][x] * T[y+bok-1][x] * T[y][x+bok-1] * T[y+bok-1][x+bok-1]

                    if iloczyn == k:
                        return (y + y + bok - 1) // 2, (x + x + bok - 1) // 2

    return False

T = [ [1,2,3,4,5],
      [5,6,7,8,3],
      [9,10,11,12,4],
      [13,14,15,16,1],
      [4, 3, 5, 3, 1] ]

print(zad9(T, 8347384732))