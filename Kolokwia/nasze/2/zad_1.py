
def check(ogr):
    N = len(ogr)
    w, k = 0, 0
    kierunek = 2
    skok = [(-1,0), (0,1), (1,0), (0,-1)]
    
    # / 
    P = [1, 0, 3, 2]

    # \
    L = [3, 2, 1, 0]

    while True:
        w, k = w+skok[kierunek][0], k+skok[kierunek][1]

        if ogr[w][k] == '\\':
            kierunek = L[kierunek]
        elif ogr[w][k] == '/':
            kierunek = P[kierunek]
        elif w == k == N - 1:
            return True
        elif not (0 <= w < N and 0 <= k <= N):
            return False
        
def zamien(ogr, w, k):
    if ogr[w][k] == '\\':
        ogr[w][k] = '/'
    else:
        ogr[w][k] = '\\'

def napraw(ogr):
    N = len(ogr)
    zwierciadla = []
    for w in range(N):
        for k in range(N):
            if ogr[w][k] != '.':
                zwierciadla.append((w,k))

    for i in range(N-1):
        zamien(ogr, zwierciadla[i][0], zwierciadla[i][1])
        for j in range(i+1, N):
            zamien(ogr, zwierciadla[j][0], zwierciadla[j][1])
            if check(ogr):
                return 
            
            zamien(ogr, zwierciadla[j][0], zwierciadla[j][1])
        zamien(ogr, zwierciadla[i][0], zwierciadla[i][1])
    
    print('error')
    