class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def zad23(p):
    slow = p
    fast = p
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    cnt = 1
    slow = slow.next
    while slow != fast:
        slow = slow.next
        cnt += 1
    return cnt

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = d

print(zad23(a))