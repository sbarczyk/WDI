def interference(A, B):
    return A[0] <= B[1] <= A[1] or A[0] <= B[0] < A[1]

def zad_2(T):
    n = len(T)
    U = [0] * n
    
    def rek(i, suma, cnt):
        if suma == 2022:
            return True
        if suma > 2022:
            return False
        if i == n:
            return False
        
        for k in range(cnt):
            if interference(T[i], T[U[k]]):
                break
        else:
            U[cnt] = i
            if rek(i+1, suma + T[i][1] - T[i][0], cnt +1):
                return True
            return rek(i+1, suma, cnt)
        
        return rek(i+1, suma, cnt)
    
    return rek(0,0,0)


T = [(1, 2021), (3, 2026), (2022, 2024), (2024, 2028)]
print(zad_2(T))