def check_seq(beg, end, T):
    if end >= len(T) - 1:
        return False

    mult = T[end + 1] / T[beg]
    
    for x in range(end - beg + 1):
        if end + x + 1 >= len(T) or T[end + x + 1] / T[beg + x] != mult:
            return False
    return True

def zad_1(T):
    n = len(T)
    for beg in range(n):
        for length in range(n, 2, -1):
            if check_seq(beg, beg + length - 1, T):
                return beg, beg + length - 1
            
    return 0
T = [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]
print(zad_1(T))