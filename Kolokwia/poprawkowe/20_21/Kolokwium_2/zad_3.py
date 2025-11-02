""" Lista zawiera wartości będące liczbami naturalnymi Proszę napisać funkcję repair(p), 
(p wskazuje na pierwszy element listy) która przekształca listę 
tak aby liczby parzyste znalazły się na końcu listy. Funkcja powinna zwrócić 
wskazanie na przekształconą listę. """


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def repair(p):
    g = Node(None, p)
    even = Node()
    p = g
    
    while p.next is not None:
        if p.next.value % 2 == 0:
            tmp = p.next
            p.next = p.next.next
            tmp.next = even.next
            even.next = tmp
        else:
            p = p.next

    p.next = even.next
    return g.next

def list_to_linked_list(lst):
    g = Node()
    for elem in lst[::-1]:
        new_node = Node(elem, g.next)
        g.next = new_node
    return g.next

def print_all(p):
    while p is not None:
        print(str(p.value) + ' ->', end=' ')
        p = p.next
    print("KONIEC")
    print()

q = list_to_linked_list([2, 5, 7, 8, 9, 0, 1])
print_all(q)
x = repair(q)
print_all(x)

