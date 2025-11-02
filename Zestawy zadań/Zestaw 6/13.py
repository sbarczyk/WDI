class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete(p):
    if p.next is not None:
        delete(p.next)
        if p.next.value < p.value:
            p.next = p.next.next
    