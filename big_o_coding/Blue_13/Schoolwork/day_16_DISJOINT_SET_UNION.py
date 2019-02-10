MAX = 20
parent = []

def makeSet():
    global parent
    parent = [i for i in range(MAX + 5)]

def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

if __name__ == "__main__":
    Q = int(input())
    makeSet()
    for i in range(Q):
        u, v, q = map(int, input().split())
        if q == 1:
            unionSet(u, v)
        if q == 2:
            parentU = findSet(u)
            parentV = findSet(v)
            if parentU == parentV:
                print(1)
            else:
                print(0)
    
    
    