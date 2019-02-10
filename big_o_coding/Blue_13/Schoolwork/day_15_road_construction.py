import queue
INF = 1e9

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def MST():
    ans = 0
    for i in range(m+1):
        if path[i] == -1:
            continue
        ans += dist[i]
    return ans
    
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
    t = int(input())
    print(" ")
    m = int(input())
    graph = [[] for i in range(m+1)]
    dist = [INF for i in range(m+1)]
    path = [-1 for i in range(m+1)]
    visited = [False for i in range(m+1)]
    for i in range(m):
        u, v, w = input().split()
        u, v = ord(u), ord(v)
        graph[u].append(Node(v, int(w)))
        graph[v].append(Node(u, int(w)))
    Prim(u)
    for i in range(u):
        if dist[u] == INF:
            visited[u] = False
            print("Case {}: Impossible".format(t))
        else:
            print(sum(dist))  
# input m
# input cities
# city.id = id
# prim algo
# with each u:
#   if dist[u] = INF:
#   visited[u] = False
# print(impossible)
# print(sum(dist))
