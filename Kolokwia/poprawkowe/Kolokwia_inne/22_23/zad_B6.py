class Node:
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next

def separate(p):
    g = Node(None, p)
    even = Node(None)
    odd = Node(None)
    counter = 0

    while g.next is not None:
        if g.next.value > 0 and g.next.value % 2 == 0:
            tmp = g.next
            g.next = g.next.next
            tmp.next = even.next
            even.next = tmp

        elif g.next.value < 0 and g.next.value % 2 == 1:
            tmp = g.next
            g.next = g.next.next
            tmp.next = odd.next
            odd.next = tmp

        else:
            tmp = g.next
            g.next = g.next.next
            counter += 1

    return odd.next, even.next, counter


def print_list(head):
    while head is not None:
        print(str(head.value) + ' -> ', end = '')
        head = head.next
    print('KONIEC')


def list_to_linked_list(list):
    g = Node()
    for elem in list[::-1]:
        new_node = Node(elem, g.next)
        g.next = new_node
    return g.next
            

q = list_to_linked_list([2,-3,4,6,7,9,-5])
print_list(q)
a,b,res = separate(q)
print_list(a)
print_list(b)
print(res)
