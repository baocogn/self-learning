k = int(input())

l = []
for i in range(1, k+1):
    l.append(i)

pairs = 0

if k % 2 == 0:
    pairs = len(l) / 2
