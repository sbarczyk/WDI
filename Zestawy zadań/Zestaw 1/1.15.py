
from math import sqrt
def pi(accuracy):
    pi = 2
    a = sqrt(0.5)
    for i in range (accuracy):
        pi /= a
        a = sqrt(0.5+0.5*a)
    return pi

print(pi(1000))