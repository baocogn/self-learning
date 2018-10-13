n, t = map(int, input().split())
a = list(map(int, input().split()))[:n]
res, time, count, j = 0, 0, 0, 0

for i in range(n):
    time += a[i]
    count += 1
    while time > t:
        time -= a[j]
        j += 1
        count -= 1
    if res < count:
        res = count

print(res)

# choose i, then choose j to the left of i (if sum(a[i], a[j]) <= t)
# when i = 0: time += a[0] = 3, count = 1