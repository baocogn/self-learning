class Package:
    def __init__(self, id_number, weight):
        self.id_number = id_number
        self.weight = weight

class Node:
    def __init__(self, data=Package("", 0)):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, id_number, weight):
        p = Node(Package(id_number, weight))
        if self.head == self.tail == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    
    def max(self):    
        if self.head == None:
            return None
        res = self.head
        cur = self.head
        while cur != None:
            if cur.data > res.data:
                res = cur
            cur = cur.next
           
        return res.data
        
l = LinkedList()

while True:
    raw_input = input().split()
    id_number = raw_input[0]    
    weight = int(raw_input[1])
    
for id_number, weight in raw_input:
    if id_number == weight == 0:
        break
    l.insertTail(id_number, weight)

print(l.max())     