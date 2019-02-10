import queue
INF = 1e9

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def printMST():
    ans = 0
    for i in range(n+1):
        if path[i] == -1:
            continue
        ans += dist[i]
        # print("{0} - {1}: {2}".format(path[i], i, dist[i]))
    print(ans)

def Prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        d = top.dist
        visited[u] = True
        for neigbor in graph[u]:
            v = neigbor.id
            w = neigbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    dist = [INF for i in range(n+1)]
    path = [-1 for i in range(n+1)]
    visited = [False for i in range(n+1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))
    Prim(1)
    printMST()
