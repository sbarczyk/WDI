""" Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, 
przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym. """
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def wypisz(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next 


def check(x):
    cnt = 0
    while x != 0:
        if x % 8 == 5:
            cnt += 1
            x //= 8
    return cnt % 2 == 0

def zad_16(head):
    guard = Node(None)
    guard.next = head
    curr = guard
    while curr.next is not None:
        if check(curr.next.val):
            to_move = curr.next
            curr.next = curr.next.next
            to_move.next = guard.next
            guard.next = to_move
        else:
            curr = curr.next
    return guard.next

a = Node(2)
b = Node(3)
c = Node(5)
d = Node(7)
e = Node(11)
a.next = b
b.next = c
c.next = d
d.next = e

print("Przed przeniesieniem:")
wypisz(a)

res = zad_16(a)

print("\nPo przeniesieniu:")
wypisz(res)




