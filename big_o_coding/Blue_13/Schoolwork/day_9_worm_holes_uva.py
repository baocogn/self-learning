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
        for edge in graph:
            u = edge.source
            v = edge.target
            w = edge.weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
    for edge in graph:
        u = edge.source
        v = edge.target
        w = edge.weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True

if __name__ == '__main__':
    c = int(input())
    for _ in range(c):
        n, m = map(int, input().split())
        graph = []
        dist = [INF for i in range(n+5)]
        path = [-1 for i in range(n+5)]
        for i in range(m):
            u, v, w = map(int, input().split())
            graph.append(Edge(u, v, w))
        s = 0
        res = BellmanFord(s)
        # for t in range(1, m):
            # res = dist[t]
        if res == False: # in this quiz, if the year is negative, then people can go back to the past
            print("possible")
        else:
            print("not possible") 
    