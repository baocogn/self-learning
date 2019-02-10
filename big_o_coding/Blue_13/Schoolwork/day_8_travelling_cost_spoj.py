import queue
MAX = 100
INF = int(1e9)
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u

if __name__ == '__main__':
    n = int(input())
    graph = [[] for i in range(n+5)]
    
    for _ in range(n):
        a, b, w = map(int, input().split()) 
        graph[a].append(Node(b, w))
        graph[b].append(Node(a, w))
    
    dist = [INF for i in range(n+5)]
    path = [-1 for i in range(n+5)]
    
    s = int(input())
    q = int(input())
    for _ in range(q):
        v = int(input())
        Dijkstra(s)
        ans = dist[v]
        if ans == INF:
            print("NO PATH")
        else:
            print(ans)
            