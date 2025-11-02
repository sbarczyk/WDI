class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def zad22(pointer):
    slow = pointer
    fast = pointer
    while fast.next != None and fast.next.next != None:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False