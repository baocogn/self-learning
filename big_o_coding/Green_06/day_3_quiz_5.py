import math

x = int(input())
flag = True
if x <= 1:
    flag = False
else:
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            flag = False
            break

if flag == True:
    print("YES")
if flag == False:
    print("NO")
