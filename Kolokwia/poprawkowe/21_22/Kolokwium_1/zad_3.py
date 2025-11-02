""" Proszę napisać funkcję Two(p), która otrzymuje wskazanie na listę i rozdziela elementy listy do dwóch list. 
W pierwszej powinny znaleźć się elementy, które w liście wejściowej występowały dokładnie dwa razy, 
a w drugiej wszystkie pozostałe. Funkcja powinna zwrócić wskaźniki do powstałych dwóch list. """

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

def two(p):
    g = Node(0, p)
    
    appearing_twice = Node()
    appearing_twice_end = appearing_twice
    others = Node()
    others_end = others
    
    while p.next is not None:
        k = p.next.value
        curr = p
        new_list = Node(0, None)
        while curr.next is not None:
            if curr.next.value == k:
                tmp = curr.next
                curr.next = curr.next.next
                tmp.next = new_list.next
                new_list.next = tmp
                new_list.value = new_list.value + 1
            else:
                curr = curr.next
        
        if new_list.value == 2:
            appearing_twice_end.next = new_list.next
            while appearing_twice_end.next is not None:
                appearing_twice_end = appearing_twice_end.next
        else:
            others_end.next = new_list.next
            while others_end.next is not None:
                others_end = others_end.next

    return appearing_twice.next, others.next

def list_to_linked_list(list):
    g = Node()
    for elem in list[::-1]:
        new_node = Node(elem, g.next)
        g.next = new_node
    return g

def print_all(p):
    while p is not None:
        print(str(p.value) + ' ->', end = ' ')
        p = p.next
    print("KONIEC")
    print()


q = list_to_linked_list([2,3,5,2,5,7,9,8])
print_all(q)
a, b = two(q)
print_all(a)
print_all(b)




            
        


