""" Zadanie 15. 
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, 
usuwa z niej wszystkie elementy, w których wartość klucza w zapisie trójkowym ma większą ilość jedynek 
niż dwójek. """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def check(x):
    jedynki = 0
    trojki = 0
    while x != 0:
        if x % 3 == 1:
            jedynki += 1
        elif x % 3 == 2:
            trojki += 1
        x //= 3

    return jedynki > trojki

def zad_15(head):
    g = Node(None)
    g.next = head
    curr = g

    if head is None:
        return
   
    while curr.next != None:
        if check(curr.next.value):
            curr.next = curr.next.next
        else:
            curr = curr.next