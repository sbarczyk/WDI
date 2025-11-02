class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def repair(p):
    guardian = Node(None, p)
    head = guardian
    even_numbers = Node()

    while head.next is not None:
        if head.next.val % 2 == 0:
            tmp = head.next
            head.next = head.next.next
            tmp.next = even_numbers.next
            even_numbers.next = tmp
        else:
            p = p.next
    
    head.next = even_numbers.next
    return guardian.next
