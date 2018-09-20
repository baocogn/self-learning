class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, x):
        p = Node(x)
        if self.head == self.tail == None:
            self.head = self.tail = Node(x)
        else:
            self.tail.next = p
            self.tail = p

    def insert_ord_num(self):
        if self.head == None:
            return
        
        p = Node(1)
        p.next = self.head
        self.head = p

        count = 2
        cur = p.next
        while cur.next:
            p = Node(count)
            p.next = cur.next
            cur.next = p
            cur = p.next
            count += 1

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next

a = list(map(int, input().split()))
l = LinkedList()
for x in a:
    if x == 0:
        break
    else:
        l.insertTail(x)

l.insert_ord_num()
l.print_list()
