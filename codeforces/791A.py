a, b = map(int, input().split())

limak = a * 3
bob = b * 2

cnt = 1
while limak <= bob:
    limak *= 3
    bob *= 2
    cnt += 1
print(cnt)
