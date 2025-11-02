def sequence(T):
    n = len(T)
    max1 = None
    max2 = None
    for length in range(n - 1, 4, -1):
        for start in range(1, n - 2):
            if start + length >= len(T):
                break
            
            valid = True
            for i in range(length-1):
                if T[start+i] > T[start+i+1]:
                    valid = False
                    break
            
            if valid:
                if max1 is None:
                    max1 = (start, length - start + 1)
                    print(max1)
                elif max2 is None:
                    max2 = (start, length - start + 1)
                    print(max2)
            
            if max1 is not None and max2 is not None:
                return (max2[0] > max1[1] or max1[0] > max2[1])
    
    return False  
                

print(sequence([2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]))
