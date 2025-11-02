class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def zad24(p):
    slow = p
    fast = p
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = p
    cnt = 0
    while slow != fast:
        slow = slow.next
        fast = fast.next
        cnt += 1
    return cnt