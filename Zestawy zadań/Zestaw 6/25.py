class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def zad23(p):
    slow = p
    fast = p
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = p
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    return slow.value