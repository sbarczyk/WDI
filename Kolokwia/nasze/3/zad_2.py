class Node:
    def __init__(self, value = None, next = None):
        self.next = next
        self.value = value


def czy_rosnacy(str):
    n = len(str)
    for i in range(0, n-1):
        if ord(str[i]) >= ord(str[i+1]):
            return False
    return True

def czy_malejacy(str):
    n = len(str)
    for i in range(0, n-1):
        if ord(str[i]) <= ord(str[i+1]):
            return False
    return True


def make_order(p):
    g = Node(None, p)
    p = g
    start = g
    rosnace = Node(None)
    rosnace_start = rosnace
    malejace = Node(' ')
    malejace_start = malejace
    inne = Node(' ')
    inne_start = inne
    
    while p.next is not None:
        a = str(p.next.value)
        if czy_malejacy(a):
            tmp = p.next
            p.next = p.next.next
            tmp.next = malejace.next
            malejace.next = tmp
        elif czy_rosnacy(a):
            tmp = p.next
            p.next = p.next.next
            tmp.next = rosnace.next
            rosnace.next = tmp
        else:
            tmp = p.next
            p.next = p.next.next
            tmp.next = inne.next
            inne.next = tmp

    g.next = rosnace_start.next
    while g.next is not None:
        g = g.next
    g.next = inne_start
    while g.next is not None:
        g = g.next
    g.next = malejace_start

    return start.next

def list_to_linked_list(list):
    g = Node()
    for elem in list[::-1]:
        new_node = Node(elem, g.next)
        g.next = new_node
    return g.next

def print_list(head):
    while head != None:
        print(str(head.value) + ' -> ', end = '')
        head = head.next

q = list_to_linked_list(['ala', 'ola', 'abel', 'ula', 'irys', 'ewa', 'sroka', 'gips'])
res = make_order(q)
print_list(res)
            

            

        

