class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()
    
def addWord(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
    tmp.countWord += 1

def findWord(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return False
        tmp = tmp.child[ch]
    return tmp.countWord > 0

if __name__ == "__main__":
    root = Node()
    addWord(root, "hello")
    addWord(root, "bigo")

    print(findWord(root, "hello"))
