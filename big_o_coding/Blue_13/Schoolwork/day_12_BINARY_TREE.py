# complexity: O(2logn)
class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None
    
def createNode(x):
    newNode = Node()
    newNode.key = x
    return newNode

def insertNode(root, x):
    if root == None:
        return x.createNode()
    if x < root.key:
        root.left = insertNode(root.left, x)
    elif x > root.key:
        root.right = insertNode(root.right, x)

class BST:
    def __init__(self):
        self.root = None

    def add(self, x):
        if self.root == None:
            self.root.Node(x)
        else:
            self.root.add(x)
