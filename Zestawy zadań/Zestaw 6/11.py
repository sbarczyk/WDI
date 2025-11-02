class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def print_all(p):
    while p.next != None:
        print(p.next.value)
        p = p.next


def zad_11(p, value):
    while p.next != None:
        if p.next.value == value:
            p.next = p.next.next
            return
        p = p.next
    a = Node(value)
    p.next = a

g = Node(None)
a = Node(3)
b = Node(7)
c = Node(159)

g.next = a
a.next = b
b.next = c

print_all(g)
zad_11(g, 19)
print('--')
print_all(g)
