class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

def repair(p):
    
    r = p.next.value - p.value
    curr = p
    
    while curr.next is not None:
        if curr.next.value - curr.value == r:
            curr = curr.next
        else:
            missing_value = curr.next.value - r
            new_node = Node(missing_value, curr.next)
            curr.next = new_node
    return p

def list_to_linked_list(list):
    g = Node()
    for elem in list[::-1]:
        new_node = Node(elem, g.next)
        g.next = new_node
    return g.next

def print_all(p):
    while p is not None:
        print(str(p.value) + ' ->', end = ' ')
        p = p.next
    print("KONIEC")
    print()

q = list_to_linked_list([1,3,7,11,15])
print_all(q)
a = repair(q)
print_all(a)