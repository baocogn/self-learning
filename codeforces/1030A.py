n = int(input())
l = list(map(int, input().split()))

cnt0 = 0
for i in range(len(l)):
    if l[i] == 0:
        cnt0 += 1
if cnt0 < len(l):
    print("HARD")
else:
    print("EASY")
