class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_all(p):
    while p.next is not None:
        print(p.next.value)
        p = p.next


def zad_18(p):
    values = []
    values_to_delete = []
    head = p
    while p.next is not None:
        if p.next.value not in values:
            values.append(p.next.value)
        else:
            if p.next.value not in values_to_delete:
                values_to_delete.append(p.next.value)
        p = p.next
    p = head
    while p.next is not None:
        if p.next.value in values_to_delete:
            p.next = p.next.next
        else:
            p = p.next
        


g = Node(None)
a = Node(3)
b = Node(7)
c = Node(3)
d = Node(7)
e = Node(313)


g.next = a
a.next = b
b.next = c
c.next = d
d.next = e

print_all(g)
zad_18(g)
print('--')
print_all(g)