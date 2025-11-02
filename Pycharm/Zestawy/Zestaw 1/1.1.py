def fibonacci():
    a1 = 1
    a2 = 1
    while True:
        if a1 < 1000000:
            print(a1)
            a1, a2 = a2, a1 + a2
        else:
            break
fibonacci()
