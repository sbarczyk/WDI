class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

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

def common_part(p, q):
    new_list = Node()
    start = new_list
    
    while p.next and q.next is not None:
        if p.next.value > q.next.value:
            q = q.next
        elif q.next.value > p.next.value:
            p = p.next
        else:
            tmp = p.next
            p.next = p.next.next
            tmp.next = None
            new_list.next = tmp
            new_list = new_list.next
    return start

def iloczyn(a, b, c):
    return common_part(a, common_part(b, c))
    
    
    

p = list_to_linked_list([2,3,4,5])
q = list_to_linked_list([2,5])
x = list_to_linked_list([5])
res = iloczyn(p, q, x)
print_all(res)