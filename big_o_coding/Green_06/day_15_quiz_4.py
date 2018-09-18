class Edge:
    def __init__(self, u, v, w):
        self.u = u 
        self.v = v
        self.w = w 

m = int(input())

edge_list = []

minw = 99999

count=0
for i in range(0, m, 1):
    a = list(map(int, input().split()))
    if len(a) > 3:
        break
    else:
        edge_list.append(Edge(a[0],a[1],a[2]))
    if a[2] < minw:
        minw = a[2]
    if a[2] == minw:
        count = minw + minw
print(count)
