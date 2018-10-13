m = int(input())
a = []
for _ in range(m):
    row = list(map(int, input().split()))
    a.append(row)

flag = True
for i in range(0, m, 1):
    for j in range(0, m, 1):
        if a[i][j] != a[j][i]:
            flag = False
    
if flag == True:
    print("YES")
else:
    print("NO")