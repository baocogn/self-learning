m, n = list(map(int, input().split()))

a = []
for _ in range(m):
    row = list(map(int, input().split()))
    a.append(row)

count = 0

for j in range(0, m, 1):
    if a[n][j] != 0:
        count += 1

print(count)