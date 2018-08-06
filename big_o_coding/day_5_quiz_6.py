n = int(input())
a = list(map(int, input().split()))

energy = 0
min_h = a[0]

for i in range(len(a)):
    if a[i] < min_h:
        min_h = a[i]

for x in a:
    energy += x - min_h

print(energy)
    