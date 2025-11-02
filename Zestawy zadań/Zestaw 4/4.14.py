def l_jedynek(a):
    liczba_jedynek = 0
    while a > 0:
        if a % 2 == 1:
            liczba_jedynek += 1
        a //= 2
    return liczba_jedynek
print(l_jedynek(22))

def compare(a,b):
    return l_jedynek((a)) == l_jedynek(b)

def zad14(N1, N2):
    for i in range(len(N2)-len(N1)+1):
        for j in range(len(N2)-len(N1)+1):
            counter = 0
            for x in range(len(N1)):
                for y in range(len(N1)):
                    if compare(N1[i+x][j+y], N2[x][y]):
                        counter += 1
            if counter / (len(N1)**2) > 0.33:
                return True
    return False

print(zad14(T1,T2))
