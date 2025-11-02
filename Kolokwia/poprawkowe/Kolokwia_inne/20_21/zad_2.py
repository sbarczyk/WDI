def compare(A, B):
    for x in range(len(A)):
        if A[x] != B[x]:
            return 1 if A[x] == 1 else -1
        

def distance(T):
    n = len(T)
    max_ind = 0
    min_ind = 0
    
    for i in range(n):
        if compare(T[i], T[max_ind]) == 1:
            max_ind = i
        elif compare(T[min_ind], i) == 1:
            min_ind = i
    
    return abs(max_ind - min_ind)