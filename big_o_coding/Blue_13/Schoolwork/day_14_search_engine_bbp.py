class Node:
    def __init__(self):
        self.maxValue = 0
        self.child = dict()
    
def addWord(root, s, value):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
        tmp.maxValue = max(tmp.maxValue, value)

def findWord(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return 0
        tmp = tmp.child[ch]
    return tmp.maxValue

if __name__ == "__main__":
    root = Node()
    n, q = map(int, input().split())
    for _ in range(n):
        s, w = input().split()
        addWord(root, s, int(w))
    for _ in range(q):
        t = input()
        if findWord(root, t) != 0:
            print(findWord(root, t))
        else:
            print(-1)
