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
    
    def min(self):
        if self.left == None:
            return self.data
        else:
            return self.left.min()

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, x):
        if self.root == None:
            self.root = Node(x)
        else:
            self.root.add(x)
    
    def min(self):
        return self.root.min()
    
n = int(input())
a = list(map(int, input().split()))
l = BST()

for number in a:
    if len(a) > n:
        break
    l.add(number)

print(l.min())
    