def nwd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def nwd_3(a,b,c):
    return nwd(nwd(a,b), c)


def trojki(T):
    n = len(T)
    found = []
    counter = 0
    for i in range(n-2):
        for j in range(i+1, i+3):
            if j < n:
                if nwd(T[i], T[j]) == 1:
                    for k in range(j+1, j+3):
                        if k < n:
                            if nwd(T[j], T[k]) == nwd(T[i], T[k]) == 1:
                                found.append((T[i], T[j], T[k]))
                                counter += 1

    print(found)
    return counter

print(trojki([2,3,4,5,6,8,7]))