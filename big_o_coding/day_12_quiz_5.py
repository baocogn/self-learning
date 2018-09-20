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

    def delete_end_with_5(self):
        tmp = Node()
        tmp.next = self.head

        prev = tmp
        cur = self.head
        while cur != None:
            if cur.data % 10 == 5:
                if cur == self.tail:
                    self.tail = prev
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        self.head = tmp.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next

n = int(input())
a = list(map(int, input().split()))[:n]
l = LinkedList()

for x in a:
    l.insertTail(x)

l.delete_end_with_5()
l.print_list()
