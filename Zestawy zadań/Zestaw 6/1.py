class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next


def add(p, new_val):
    if p.next is None:
        q = Node(new_val)
        p.next = q
    
    if p.next is not None:
        if p.next.val == new_val:
            return
    
        elif p.next.val > new_val:
            q = Node(new_val)
            q.next = p.next
            p.next = q
        
        else:
            add(p.next, new_val)


def is_present(g, val):
    if g.next is None:
        return False
    if g.next.val == val:
        return True
    if g.next.val > val:
        return False
    return is_present(g.next, val)


def delete(g, val):
    if g.next is None:
        return
    if g.next.val == val:
        g.next = g.next.next
    elif g.next.val < val:
        delete(g.next, val)
    

    

        

