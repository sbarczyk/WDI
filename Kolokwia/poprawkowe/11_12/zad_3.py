class Node:
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next

def add_to_list(p, val):
    start = p
    head = p.next
    head_prev = p
    first_digit = str(val)[0]
    last_digit = str(val)[-1]
    
    while True:
        curr_first_digit = str(head.value)[0]
        next_last_digit = str(head.next.value)[-1]
        if curr_first_digit == first_digit and next_last_digit == last_digit:
            new_node = Node(val)
            new_node.next = head.next.next
            head_prev.next = new_node
            return True
        head_prev = head
        head = head.next
        if head == start:
            break
    return False

def list_to_cycle_linked_list(list):
    head = Node(list[0])
    start = head
    for i in range(1, len(list)):
        head.next = Node(list[i])
        head = head.next
    head.next = start
    return start

q = list_to_cycle_linked_list([123, 324, 435, 578])
res = add_to_list(q, 35)
print(res)
            
        

