class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def czy_l_jedynek_niep(x):
    counter = 0
    while x > 0:
        if x % 2 == 1:
            counter += 1
            print(counter)
        x //= 2
    return counter % 2 == 1

def usun_elementy(head):
    p = head
    i = head
    while i.next != None:
        i = i.next
        if not czy_l_jedynek_niep(i.value):
            p.next = i
            p = p.next
    p.next = None