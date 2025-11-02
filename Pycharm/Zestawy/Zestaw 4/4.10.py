def zero_check(T):
 n = len(T)
 columns = [0] * n

 for y in range(n):
    flag = False
    for x in range (n):
         if T[y][x] == 0:
             flag = True
             columns[x] += 1
    if not flag:
        return False

 for element in columns:
    if element == 0:
        return False
    return True

tab = [ [1,2,3,0],
        [120,0,96,0],
        [8,13,0,9],
        [0,9503,0,140]
        ]

print( zero_check(tab) )