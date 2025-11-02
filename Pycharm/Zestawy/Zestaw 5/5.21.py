def zad21(T, target):

    def rek(suma, W, K):
        if suma == target != 0:
            return True
        if suma > target:
            return False

        for y in range(8):
            if W[y]:
                for x in range(8):
                    if K[x]:
                        W[y] = False
                        K[x] = False
                        if rek(suma + T[y][x], W, K):
                            return True
                        else:
                            W[y] = True
                            K[x] = True

        return False
    return rek(0, [True] * 8, [True] * 8)








