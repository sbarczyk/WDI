def liczba_jedynek(x):
    counter = 0
    while x > 0:
        if x % 2 == 1:
            counter += 1
        x //= 2
    return counter

def zad_2(tab):
    def rek(i, a, b, c):
        if i == len(tab):
            if a == b and b == c:
                print(a)
                return True
            return False
        
        return rek(i+1, a + liczba_jedynek(tab[i]), b, c) or \
            rek(i+1, a, b + liczba_jedynek(tab[i]), c) or \
                rek(i+1, a, b, c + liczba_jedynek(tab[i]))
    return rek(0,0,0,0)
    
print(zad_2([2, 3, 5, 7, 11, 13, 16]))