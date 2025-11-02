class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


def print_all(p):
    if p is None:
        print("KONIEC")
        return

    while p is not None:
        print(str(p.value) + ' ->', end=' ')
        p = p.next
    print("KONIEC")
    print()


def zad_3(p):
    g = Node(None, p)
    head = g
    
    first = Node()
    first_end = first
    second = Node()
    second_end = second
    third = Node()
    third_end = third
    forth = Node()
    forth_end = forth

    while head.next is not None:
        
        if head.next.value[0] == 0 or head.next.value[1] == 0:
            head.next = head.next.next
        
        elif head.next.value[0] > 0:
            
            if head.next.value[1] > 0:
                tmp = head.next
                head.next = head.next.next
                tmp.next = None
                first_end.next = tmp
                first_end = first_end.next

            else:
                tmp = head.next
                head.next = head.next.next
                tmp.next = None
                forth_end.next = tmp
                forth_end = forth_end.next

        else: 
            if head.next.value[1] > 0:
                tmp = head.next
                head.next = head.next.next
                tmp.next = None
                second_end.next = tmp
                second_end = second_end.next
            
            else:
                tmp = head.next
                head.next = head.next.next
                tmp.next = None
                third_end.next = tmp
                third_end = third_end.next
        


    return first.next, second.next, third.next, forth.next


def list_to_linked_list(lst):
    g = Node()
    for elem in lst[::-1]:
        new_node = Node(elem, g.next)
        g.next = new_node
    return g.next

q = list_to_linked_list([(1,2), (-1,1), (1,-1), (-1,-1), (1,0), (0,1), (-1,2), (-5,3)])
print_all(q)

(a, b, c, d) = zad_3(q)

print_all(a)
print_all(b)
print_all(c)
print_all(d)    
