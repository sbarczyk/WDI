def nwd(a,b):
    while b != 0:
        a, b = b, a%b
    return a


def nww(a,b):
    return (a*b)//nwd(a,b)

def nww3(a, b, c):
    return nww(nww(a, b), c)

print(nww3(100,200,300))