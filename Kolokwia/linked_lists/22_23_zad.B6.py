class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def zad_B6(p):
    run = p
    even = Node(None)
    odd = Node(None)
    while True:
        if not run.value % 2 and run.value > 0:
                even.next = run 
                even = even.next
        if run.value % 2 and run.value < 0:
                odd.next = run 
                odd = odd.next
        if run.next == p:
            break
        run = run.next
 
    return even.value, odd.value