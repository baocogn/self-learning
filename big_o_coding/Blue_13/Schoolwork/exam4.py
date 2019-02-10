# Phone List
class TrieNode:
    def __init__(self):
        self.count_leaf = 0
        self.child = dict()
        self.pre_check = False
 
class Trie:
    def __init__(self):
        self.root = TrieNode()
 
    def add_word(self, s):
        cur = self.root
        flag = True
        for c in s:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur.pre_check = True
            cur = cur.child[c]
            if cur.count_leaf != 0:
                flag = False
        cur.count_leaf += 1
        if cur.pre_check:
            flag = False
        return flag
 
TC = int(input())
for t in range(TC):
    n = int(input())
    trie = Trie()
    check = True
    for i in range(n):
        s = input().strip()
        check = check and trie.add_word(s)
 
    if check:
        print('Case {}: YES'.format(t+1))
    else:
        print('Case {}: NO'.format(t+1))
