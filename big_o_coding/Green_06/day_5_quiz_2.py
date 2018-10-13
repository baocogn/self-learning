n = int(input())
a = list(map(float, input().split()))

ans = a[0]
for i in range(len(a)):
    if a[i] > ans:
        ans = a[i]

print(ans)
