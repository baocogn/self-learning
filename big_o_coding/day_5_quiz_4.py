n = int(input())
a = list(map(int, input().split()))

flag = True
for i in range(len(a)):
    if a[i] <= 0:
        flag = False

if flag == True:
    print("YES")
else:
    print("NO")