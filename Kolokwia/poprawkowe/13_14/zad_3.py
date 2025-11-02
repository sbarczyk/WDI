""" Napisz funkcję, która przyjmuje wskaźnik do początku jednokierunkowego łańcucha odsyłaczowego, 
a następnie przenosi na początek wszystkie elemen- ty, w których zapisie ósemkowym występuje 
nieparzysta liczba piątek. """


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

def liczba_piatek(x):
    counter = 0
    while x > 0:
        if x % 8 == 5:
            counter += 1
        x //= 8
    return counter

def zad_3(p):
    g = Node(None, p)
    start = g
    head = g

    while head.next is not None:
        x = head.next.value
        if liczba_piatek(x) % 2 == 1:
            temp = head.next
            head.next = head.next.next
            temp.next = start.next
            start.next = temp
        else:
            head = head.next
    return g.next


def print_all(p):
    if p is None:
        print("KONIEC")
        return

    while p is not None:
        print(str(p.value) + ' ->', end=' ')
        p = p.next
    print("KONIEC")
    print()

def list_to_linked_list(tab):
    p = Node()
    end = p
    for i in range(len(tab)):
        end.next = Node(tab[i])
        end = end.next
    return p.next

tab = [5, 8, 15, 22, 58, 85, 105]
a = list_to_linked_list(tab)
print_all(a)
print_all(zad_3(a))

