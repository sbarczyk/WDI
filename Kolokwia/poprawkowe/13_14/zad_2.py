def rek(i, T, cnt):
    if i == len(T) - 1:
        return cnt
    
    x = T[i]
    div  = 2
    res = -1
    
    while x != 1:
        if x % div == 0  and i + div < len(T):
            temp_res = rek(i+div, T, cnt+1)
            if temp_res != -1:
                res = temp_res
        while x % div == 0:
            x //= div
        
        div += 1
    else:
        return res


T = [5, 2, 3, 2, 5, 2, 7, 2]
print(rek(0, T, 0))
