# Dana jest tablica booli. Jeżeli na danym polu szachownicy stoi figura to ma ona wartość true. Sprawdź czy skoczek
# może przemieścić się z wiersza 0 do wiersza N-1, jeżeli może on poruszać się tylko po polach pustych. Skoczek z
# każdym ruchem powinien przybliżać się do N-1 wiersza. Funkcja powinna zwrócić njmniejszą możliwą liczbę ruchów.

def zad(T):
    n = len(T)

    def rek(w, k, cnt):
        if w == n - 1:
            return cnt
        if T[w][k]:
            return float('inf')
        if k < 0 or w >= n or k >= n:
            return float('inf')

        return min((rek(w+1, k-2, cnt+1)), rek(w+1, k+2, cnt+1), rek(w+2,k-1, cnt+1), rek(w+2, k+1, cnt+1))

    best_path = float('inf')
    for k in range(len(T)):
        best_path = min(best_path, rek(0, k, 0))
    return best_path
