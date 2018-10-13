from queue import Queue

MAX = 100
V = None
E = None
graph = [[] for i in range(MAX)]
visited = [False] * MAX
path = [0] * MAX

def DFS(src):
    for i in range(V):
        visited[i] = False
        path[i] = -1
        s = []
        visited[src] = True
        s.append(src)

    while len(s) > 0:
        u = s[-1]
        s.pop()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                s.append(v)
                path[v] = u
            
def printPath(s, f):
    b = []
    if f == s:
        print(f)
        return
    if path[f] == -1:
        print(-1)
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    for i in range(len(b)-1, -1, -1):
        print(b[i], end=' ')

def printPathRecursion(s, f):
    if s == f:
        print(f, end=' ')
    else:
        if path[f] == -1:
            print(-1)
        else:
            printPathRecursion(s, path[f])
            print(f, end=' ')

if __name__ == '__main__':
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    s, d = map(int, input().split())
    DFS(s)
    printPath(s, d)