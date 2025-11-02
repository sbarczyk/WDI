def parts(T):
    max_parts = 0
    
    def rek(i, suma, cnt):
        nonlocal max_parts
        if i == len(T):
            if suma == target:
                max_parts = max(max_parts, cnt + 1)
            return
            
        if suma > target:
            return
        
        if suma == target:
            rek(i, 0, cnt + 1)
        
        rek(i+1, suma + T[i], cnt)
    
    
    for i in range(1, len(T)):
        target = 0
        for x in range(0, i):
            target += T[x]
        
        rek(0, 0, 0)

    return max_parts

T = [1,2,3,1,5,2,2,2,6]
print(parts(T))
