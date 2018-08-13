m, n = tuple(map(int, input().split()))
for i in range(m):
    list_i = list(map(int, input().split()))[:n]
    print("%d: %d" % (i, sum(list_i)))
