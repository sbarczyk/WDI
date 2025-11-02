def is_in_sequence(num):
    a,b = 1,2
    while a < num:
        a, b = b, a + b - 1
    return a == num

def seq(T):
    n = len(T)
    maxi = 0
    
    for i in range(n-2):
        for j in range(n-2):
            length = 2
            k = 2
            first = T[i][j]
            if is_in_sequence(first):
                second = T[i+1][j+1]
                while i+k < n and j+k < n:
                    if T[i+k][j+k] == first + second - 1:
                        length += 1
                        first, second = second, T[i+k][j+k]
                    else:
                        break
                    k += 1
                maxi = max(maxi, length)
    
    return maxi if maxi > 2 else 0


