suma = 10000
best = (2023, 0)

for i in range(2023):
        y = 2023
        x = i
        while x > 0 and y > x:
            x, y = y-x, x
        if x + y < suma:
            suma = x + y
            best = (x, y)

print(suma, best)