k, n, w = map(int, input().split())

res = 0
i = 1

while i <= w:
    res += i*k
    i += 1  
if res <= n:
    print(0)
else:
    print(res - n)
