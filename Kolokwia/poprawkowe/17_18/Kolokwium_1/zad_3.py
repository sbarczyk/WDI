class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


def delete(p,q):
    g_p = Node(None, p)
    g_q = Node(None, q)
    curr_p = g_p
    curr_q = g_q
    
    while curr_p.next is not None and curr_q.next is not None:
        if curr_p.next.value > curr_q.next.value:
            curr_q = curr_q.next
        elif curr_p.next.value < curr_q.next.value:
            curr_p = curr_p.next
        elif curr_p.next.value == curr_q.next.value:
            curr_p.next = curr_p.next.next
            curr_q.next = curr_q.next.next
    
    return g_p.next, g_q.next

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

p = list_to_linked_list([2,5,8,9])
q = list_to_linked_list([2,3,5,9])
print_all(p)
print_all(q)

res = delete(p, q)
print_all(res[0])
print_all(res[1])
