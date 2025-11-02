class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def zad33(p, string):
    first = string[0]
    last = string[-1]
    start = p
    run = p
    while run.next != start:
        word_1 = run.value
        word_2 = run.next.value
        if ord(word_1[-1]) < ord(first) and ord[word_2[0]] > ord(last):
            a = Node(string)
            a.next = run.next
            run.next = a
            return True
        run = run.next
    return False
        