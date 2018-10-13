m, n = tuple(map(int, input().split()))
for i in range(m): #index of the rows
    list_i = list(map(int, input().split()))[:n]
    print("%d: %d" % (i, sum(list_i))) #output the index of the row and the row's sum
