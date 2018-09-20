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

    def getHeight(self):
        if self is None:
            return 0
        if self.left != None:
            hL = self.left.getHeight()
        else: 
            hL = 0
        if self.right != None:
            hR = self.right.getHeight()
        else: 
            hR = 0
        return max(hL, hR) + 1
           
class BST:
    def __init__(self):
        self.root = None
    
    def add(self, x):
        if self.root == None:
            self.root = Node(x)
        else:
            self.root.add(x)
        
    def getHeight(self):
        return self.root.getHeight()

n = int(input())
a = list(map(int, input().split()))
l = BST()

for x in a:
    l.add(x)

print(l.getHeight())
