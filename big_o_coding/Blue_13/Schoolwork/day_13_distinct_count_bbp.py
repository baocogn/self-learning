class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None

def createNode(x):
    node = Node()
    node.key = x
    return node

def createTree(a, n):
    root = None
    for i in range(n):
        root = insertNode(root, a[i])
    return root

def insertNode(root, x):
    if root == None:
        return createNode(x)
    if x < root.key:
        return insertNode(root.left, x)
    elif x > root.key:
        return insertNode(root.right, x)

def equal(root, x):
    if root == None or root.key == x:
        return root
    elif root.key < x:
        return equal(root.right, x)
    return equal(root.left, x)

def lessthan(root, x):
    if root == None or root.key < x:
        return root
    elif root.key > x:
        return lessthan(root.left, x)
    return lessthan(root.right, x)
    
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))[:n]

for a in A:
    A.createTree(a)
    A.createNode(a)
    if equal(a, x):
        print("Good")
    elif lessthan(a, x):
        print("Bad")
    else:
        print("Average")
