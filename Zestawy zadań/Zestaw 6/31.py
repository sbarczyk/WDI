class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def zad_31(Dhead, Whead1, Whead2):
    cnt = 0
    p1 = Whead1
    p2 = Whead2
    i = Dhead.next
    
    while i != None:
        if i.value % 2 == 0 and i.value > 0:
            p1.next = i
            p1 = p1.next
            i = i.next
        elif i.value % 2 == 1 and i.value < 0:
            p2.next = i
            p2 = p2.next
            i = i.next
        else:
            cnt += 1
            temp = i
            i = i.next
            temp.next = None
    p1.next = None
    p2.next = None
    return cnt

    
        


