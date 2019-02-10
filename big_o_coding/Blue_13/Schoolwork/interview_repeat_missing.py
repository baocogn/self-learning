l = list(map(int, input().split()))
b = sorted(l, reverse = False)
m = set(l)

for i in range(0, len(l)):
    if l[i] in m and i <= len(m):
        b.remove(l[i])        
    if len(b) == 1:
        print("{}, {}".format(b[0], b[0]+1))
