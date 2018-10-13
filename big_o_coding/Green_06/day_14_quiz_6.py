import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def add(self, x):
        if x < self.data:
            if self.left == None:
                self.left = Node(x)
            else:
                self.left.add(x)
        elif x > self.data:
            if self.right == None:
                self.right = Node(x)
            else:
                self.right.add(x)

    def printEvent(self):
        if self.left != None:
            self.left.printEvent()
        if self.right != None:
            self.right.printEvent()
        if self.data % 2 == 0:
            print(self.data, end = " ")
    
class BST:
    def __init__(self):
        self.root = None
    
    def add(self, x):
        if self.root == None:
            self.root = Node(x)
        else:
            self.root.add(x)
        
    def printEvent(self):
        self.root.printEvent()

n = int(input())
a = list(map(int, input().split()))
l = BST()

for x in a:
    l.add(x)

l.printEvent()
