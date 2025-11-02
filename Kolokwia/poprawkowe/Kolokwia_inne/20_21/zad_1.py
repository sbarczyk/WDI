def czy_wielokrotny(a):
    n = len(a)
    for fragment_len in range(1, n//2 +1):
        if n % fragment_len == 0:
            fragments_match = True
            for fragment_start in range(fragment_len, n, fragment_len):
                for i in range(fragment_len):
                    if a[i] != a[fragment_start + i]:
                        fragments_match = False
                        break
                    
                if not fragments_match:
                    break
            else:
                return True
    return False

print(czy_wielokrotny('ABCABCABC'))

def multi(T):
    max_len = 0
    for elem in T:
        if czy_wielokrotny(elem):
            max_len = max(max_len, len(elem))

    return max_len