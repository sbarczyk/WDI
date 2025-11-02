def is_in_fibo(x):
    a, b = 0, 1
    if a < x:
        a, b = b, a + b
    return a == x

def find_fibonacci_row(tab):
    n = len(tab)
    for row in range(n):
        for col in range(n-2):
            if tab[row][col] + tab[row][col+1] == tab[row][col+2] and is_in_fibo(tab[row][col]):
                return row
            
    return "Nie ma takiego wiersza"



tab = [
    [1, 2, 4, 4, 5],
    [1, 0, 2, 3, 4],
    [6, 7, 8, 9, 10]
]

print(find_fibonacci_row(tab))