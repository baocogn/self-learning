from queue import Queue

Max = 100
V = None
E = None
graph = [[] for i in range(Max)]
visited = [False] * Max
path = [0] * Max
dist = [-1 for i in range(Max)]

def DFS(src):
    for i in range(1, N + 1): # 1 -> N
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

def printPathRecursion(s, f):
    b = []
    if s == f:
        print(f, end=' ')
    else:
        if path[f] == -1:
            print(-1)
        else:
            b.append(printPathRecursion(s, path[f]))
            return print(len(b))
            

if __name__ == '__main__':
    N = int(input())
    for i in range(0, N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    q = int(input())
    min_a = 100
    s = 1
    DFS(s)
    for i in range(q):
        a = int(input())
 
res = printPathRecursion(s, a)


# N vertices, N-1 edges

# 1. Run BFS (the best solution),or DFS in source node
# 2. Find the number of edges from the source node to all visiting nodes.
# 3. Now pair the distance by their node.
# 4. Sort the vector of the queries.
# 5. The first node (that is the second element of a pair) of the vector is the shortest node from your root node which is also smaller in the query.
