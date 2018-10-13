n = int(input())
matrix = []
for _ in range(n):
    vertex = list(map(int, input().split()))
    matrix.append(vertex)


edge_list = []

for u in range(0, n):
    flag = True
    for v in range(0, n):
        if matrix[u][v] == 1:
            flag = False
    if flag == True:
        edge_list.append(u)
            
print(len(edge_list))
