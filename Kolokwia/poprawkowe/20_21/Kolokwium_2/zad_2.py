def czy_samogloska(chr):
    return chr in ['a', 'e', 'o', 'u', 'i', 'y']

def cutting(s):
    
    def rek(i = 0, cnt = 0):
        if i == len(s):
            return cnt
        
        if czy_samogloska(s[i]):
            cnt += 1
        
        if cnt == 2:
            return 0
        elif cnt == 1:
            return rek(i+1, 0) + rek(i+1, 1)
        else:
            return rek(i+1, 0)
        
    return rek()
        
print(cutting('sesja'))