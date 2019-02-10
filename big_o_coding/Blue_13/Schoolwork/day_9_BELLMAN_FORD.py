# complexity: O(V*E)
# use for just distance from 1 vertice to 1 vertic
MAX = 100     
INF = int(1e9)  

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

dist = []
graph = []
path = []

def BellmanFord(s):
    global dist
    global graph
    global path

    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(m):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    dist = [INF for i in range(n+5)]
    path = [-1 for i in range(n+5)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append(Edge(u, v, w))
    s, t = 0, 4
    res = BellmanFord(s)
    if res == False:
        print("No path!")
    else:
        print(dist[t]) 
