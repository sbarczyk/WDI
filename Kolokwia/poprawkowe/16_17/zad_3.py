class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def remove_common(p, q, r):
    prev_p = Node(None, p)
    prev_q = Node(None, q)
    prev_r = Node(None, r)
    counter = 0

    while p is not None and q is not None and r is not None:
        if p.value == q.value == r.value:
            prev_p.next = p.next
            prev_q.next = q.next
            prev_r.next = r.next
            counter += 1
        
        if p.value < q.value or p.value < r.value:
            prev_p = p
            p = p.next
        
        elif q.value < p.value or q.value < r.value:
            prev_q = q
            q = q.next

        else:
            prev_r = r
            r = r.next
    
    return counter

def list_to_linked_list(T):
    head = Node()
    prev = head

    for i in range(len(T)):
        prev.next = Node(T[i])
        prev = prev.next
    
    return head.next


list1 = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9,12])

list2 = list_to_linked_list([2, 4, 6, 7, 8, 9,12,15])

list3 = list_to_linked_list([3, 6, 7, 9, 12, 15])

result = remove_common(list1, list2, list3)

print(result)



