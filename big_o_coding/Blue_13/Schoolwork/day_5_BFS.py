# EDGE LIST GRAPH
from queue import Queue

MAX = 100
V = None
E = None
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]
dist = [-1 for i in range(MAX)]

def BFS(s):
    dist[s] = 0
    visited[s] = True
    q = Queue()
    q.put(s)
    while q.empty() == False:
        u = q.get()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                dist[v] = dist[u]
                q.put(v)

def printPath(s, f):
    b = []
    if f == s:
        return f
    
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    for i in range(len(b)-1, -1, -1):
        print(b[i], end = " ")
    
if __name__ == '__main__':
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 1
    f = 5
    BFS(s)
    printPath(s, f)
