# Ubiquitous religion
parent = []
 
def makeSet(n):
    global parent
    parent = [i for i in range(n)]
 
def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]
 
def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[vp] = up
 
def countSet(n):
    cnt = 0
    for i in range(n):
        if i == parent[i]:
            cnt += 1
    return cnt
 
tc = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    makeSet(n)
    for _ in range(m):
        i, j = map(int, input().split())
        unionSet(i - 1, j - 1)
    print('Case {}: {}'.format(tc, countSet(n)))
    tc += 1