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
    for _ in range(1, n):
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
    t = int(input())
    for _ in range(t):
        input()
        n = int(input())
        for _ in range(n):
            junction = map(int, input())

        m = int(input(), end="")
        for _ in range(m):
            u, v = map(int, input().split())

        # if dist[t] >= INF:
            
        # elif dist[t] < 3:
        #     print("?")



#         for _ in range(m):
#             u, v, w = map(int, input().split())
#             graph.append(Edge(u, v, w))
#         s = 0
#         res = BellmanFord(s)
#         if res == False: 
#             print
#         else:
#             print
    
# # graph = []
# #     dist = [INF for i in range(n+5)]
# #     path = [-1 for i in range(n+5)]
