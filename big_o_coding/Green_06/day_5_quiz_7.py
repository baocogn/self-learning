n = int(input())
a = list(map(int, input().split()))

count_x1 = 0
count_x2 = 0

for x in a:
    if x == 1: 
        count_x1 += 1
    else:
        count_x2 += 1
    
if count_x1 == count_x2:
    print("YES")
else:
    print("NO")
    