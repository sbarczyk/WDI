t = [[12,13,14],
     [17,14,16],
     [12,16,18]]
def only_odd(x):
    while x > 0:
        if (x % 10) % 2 == 1:
            pass
        else:
            return False
        x //= 10
    return True

def zad(t):
    for line in t:
        flag = False
        for num in line:
            if only_odd(num):
                flag = True
                break
        if not flag:
            return False
    return True

print(zad(t))



