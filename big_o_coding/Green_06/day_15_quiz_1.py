class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

m = int(input())
a = []
for _ in range(m):
    row = list(map(int, input().split()))
    a.append(row)

edge_list = []
for u in range(0, m, 1):
    for v in range(0, m, 1):
        if a[u][v] == 1 and u < v:
            edge_list.append(Edge(u, v))

print(len(edge_list))

for i in range(len(edge_list)):
    print(edge_list[i].u, edge_list[i].v)