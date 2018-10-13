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
                dist[v] = dist[u] + 6
                q.put(v)

def printPath(s, f):
    if path[f] == -1:
        return -1

    cnt = 0
    while s != f:
        cnt += 1
        f = path[f]
    return cnt * 6

if __name__ == '__main__':
    q = int(input())
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = int(input())
    BFS(s)
    print(*dist)
    exit()
    
    for f in range(1, V):
        if f != s:
            printPath(s, f)
            