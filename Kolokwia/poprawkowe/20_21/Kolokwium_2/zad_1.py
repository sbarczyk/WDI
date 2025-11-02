""" Dwie liczby naturalne są ”wspólno-czynnikowe” jeżeli w swoich rozkładach na czynniki pierwsze mają
dokładnie jeden wspólny czynnik. Na przykład: 24 i 21 albo 32 i 34. Dana jest tablica T[N][N] 
zawierająca liczby naturalne. Dwie liczby w tablicy sąsiadują ze sobą wtedy 
gdy leżą w tym samym wierszu i sąsiednich kolumnach albo leżą w tej samej kolumnie i sąsiednich wierszach. 
Proszę napisać funkcję four(T), która zwraca ilość liczb sąsiadujących z 4 liczbami wspolno-czynnikowymi. """

def czy_wspólnoczynnikowe(a, b):
    flag = False
    div = 2
    while b != 1:
        if b % div == 0:
            if a % div == 0 and not flag:
                flag = True
            elif a % div == 0 and flag:
                return False
        
        while b % div == 0:
            b //= div
        while a % div == 0:
            a //= div
        div += 1
    
    return flag

def check(y, x, T):
    return 0 <= y < len(T) and 0 <= x < len(T)

def four(T):
    neighbours = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    n = len(T)
    counter = 0
    for y in range(n):
        for x in range(n):
            for neighbour in neighbours:
                y1, x1 = neighbour
                if not check(y1, x1, T) or not czy_wspólnoczynnikowe(T[y1, x1], T[y][x]):
                    break
            else:
                counter += 1
    return counter



print(czy_wspólnoczynnikowe(32, 34))