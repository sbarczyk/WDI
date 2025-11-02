t = [[13, 12, 13],
     [2,4,13],
     [12,14,17]]
print(len(t))
def is_one_even(x):
    while x > 0:
        if (x % 10) % 2 == 0:
            return True
        x //= 10
    return False

def is_line_with_even(t, line):
    for num in t[line]:
        if not is_one_even(num):
            return False
    return True

def check_lines(t):
    for i in range(len(t)):
        if is_line_with_even(t, i):
            return True
    return False

print(check_lines(t))


