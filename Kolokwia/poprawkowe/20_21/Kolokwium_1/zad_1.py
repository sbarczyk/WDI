""" Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułamki reprezentowane 
są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję longest(T), 
zwracającą długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny. 
W przypadku gdy w tablicy nie ma ciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0.
Komentarz: Można założyć, że tablica wejściowa liczy więcej niż 2 elementy.
 """


def longest(T):
    n = len(T)
    max_length = 2

    for i in range(n - 1):
        if T[i + 1][1] * T[i][0] == 0:
            continue
        q = (T[i][1] * T[i + 1][0]) / (T[i + 1][1] * T[i][0])

        length = 2
        for index in range(i + 1, n - 1):
            if T[index + 1][1] * T[index][0] == 0:
                break
            new_q = (T[index][1] * T[index + 1][0]) / (T[index + 1][1] * T[index][0])
            if new_q != q:
                break
            
            length += 1
        
        max_length = max(max_length, length)

    return max_length if max_length > 2 else 0


print(longest([(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)]))
print(longest([(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)]))
print(longest([(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)]))
print(longest([(1,2),(2,3),(3,4),(4,5),(5,6)]))
