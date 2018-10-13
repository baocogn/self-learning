n = int(input())
a = []
b = []

for i in range(n):
	l, r = map(int, input().split())
	a.append(l)
	b.append(r)

Left = min(a)
Right = max(b)

for i in range(n):
    if a[i] == Left and b[i] == Right:
        print(i + 1)
        exit()
        
print(-1)
