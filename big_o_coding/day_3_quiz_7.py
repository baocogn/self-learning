n = int(input())
 
a = [
    [" " for _ in range(n)] for _ in range(n)        
]
 
for i in range(n):
    a[i][0]   = "*"
    a[0][i]   = "*"
    a[i][n-1] = "*"
    a[n-1][i] = "*"
 
for i in range(n):
    for j in range(n):
        print(a[i][j], end="")
    print()
