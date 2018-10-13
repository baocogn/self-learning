n = int(input())
a = list(map(int, input().split()))

ans = 0

for x in a:
    ans = ans + x

print(ans)