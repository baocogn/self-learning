MAX = 20
parent = []
cnt = []

def makeSet():
    global parent, cnt
    parent = [i for i in range(MAX + 5)]
    cnt = [1 for i in range(MAX + 5)]

def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up != vp:
        parent[up] = vp
        cnt[vp] += cnt[up]

if __name__ == "__main__":
    t = int(input())
    makeSet()
    for i in range(t):
        n, m = map(int, input().split())
        for _ in range(m):
            u, v = map(int, input().split())
            unionSet(u, v)  
        res = 0
        for i in range(1, n+1):
            res = max(res, cnt[i])
        print(res)
