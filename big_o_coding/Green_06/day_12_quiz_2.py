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
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    
    def min(self):
        if self.head == None:
            return None
        res = self.head
        cur = self.head
        while cur != None:
            if cur.data < res.data:
                res = cur
            cur = cur.next
        return res.data

a = list(map(int, input().split()))
l = LinkedList()

for x in a:
    if x == 0:
        break
    l.insertTail(x)

p = l.min()    

if p == None:
    print(0)

else:
    print(a.count(p))