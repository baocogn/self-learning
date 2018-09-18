n = int(input())
flag = True
for i in range(n):
    x = int(input())
    if x % 2 != 0:
        flag = False

if flag == True:
    print("YES")
if flag == False:
    print("NO")
    