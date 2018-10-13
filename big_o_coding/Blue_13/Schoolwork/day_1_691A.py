n = int(input())
a = list(map(int, input().split()))

flag = True
count = 0

for i in range(len(a)):
    if len(a) >= 2:
        if a[i] == 0:
            count += 1
if count != 1:
    flag = False

if n == 1:
    if a[0] == 0:
        print("NO")
    else:
        print("YES")        
elif flag == False:
    print("NO")
else:
    print("YES")