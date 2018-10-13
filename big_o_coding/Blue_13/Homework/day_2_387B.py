n, m = map(int, input().split())

a = list(map(int, input().split()))[:n]

b = list(map(int, input().split()))[:m]

j = 0
count = 0

for i in range(n):
    while j < m and b[j] < a[i]:
        j += 1
    if j < m:
        j += 1
    else:
        count += 1
