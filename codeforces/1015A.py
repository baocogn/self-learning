n, m = map(int, input().split())

segments = []
for _ in range(n):
    l_i, r_i = map(int, input().split())
    segments.append((l_i, r_i))

remains = []
for x in range(1, m+1):
    not_in = True
    for segment in segments:
        l_i, r_i = tuple(segment)
        if x >= l_i and x <= r_i:
            not_in = False
            break
    if not_in:
        remains.append(x)

print(len(remains))
for x in remains:
    print(x, end=" ")
