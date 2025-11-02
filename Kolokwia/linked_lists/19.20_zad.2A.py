class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_longest(head):
    g = Node(None)
    g.next = head

    start_long = None
    end_long = None
    len_long = 1

    curr_len = 1
    curr_start = g

    prev = g
    curr = head

    while curr is not None:
        if curr.value == curr_start.next.value:
            curr_len += 1
        
        else:
            if curr_len == len_long:
                start_long = None
                end_long = None
                len_long = 1
            elif curr_len > len_long:
                start_long = curr_start
                end_long = curr
                len_long = curr_len
            curr_len = 1
            curr_start = prev
        
        prev = curr
        curr = curr.next

    if curr_len == len_long:
        start_long = prev
        end_long = curr
        len_long = curr_len
    elif curr_len > len_long:
        start_long = curr_start
        end_long = curr
        len_long = curr_len
    
    if len_long > 1:
        start_long.next = end_long
        if start_long == g:
            if end_long is not None:
                g.value = end_long.value
                g.next = end_long.next
            else:
                g.value = None
                g.next = None
        return len_long
    return 0

def list_to_node(tab):
    p = Node(tab[0])
    curr = p
    for i in range(1, len(tab)):
        curr.next = Node(tab[i])
        curr = curr.next
    return p

def print_all(head):
    while head is not None:
        print(head.value, end=', ')
        head = head.next
    
tab = [3, 3, 3, 3, 3, 5, 7, 11, 13, 13, 1, 2, 2, 2, 2]

head = list_to_node(tab)
print(delete_longest(head))
print_all(head)
