class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_all(p):
    while p.next is not None:
        print(p.next.value)
        p = p.next

def delete(p):
    run = p.next
    while run is not None and run.next is not None:
        delete(p.next)
        if run.next.value % run.value == 0:
            run.next = run.next.next

g = Node(None)
a = Node(1)
b = Node(2)
c = Node(2)
d = Node(8)

g.next = a
a.next = b
b.next = c
c.next = d

print_all(g)
print('---')
delete(g)
print_all(g)
