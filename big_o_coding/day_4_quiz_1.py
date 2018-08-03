n = int(input())
n1 = n
n2 = n
found1 = False
found2 = True

while found1 == False:
    flag1 = True
    for i in range(2, int(n1 ** 0.5) + 1):
        if n1 % i == 0:
            flag1 = False
if flag1 == True:
    found1 = True
else:
    n1 -= 1

while found2 == False:
    flag2 = True
    for i in range(2, int(n2 ** 0.5) + 1):
        if n2 % i == 0:
            flag2 = False
if flag2 == True:
    found2 = True
else:
    n2 += 1

if n - n1 <= n - n2:
    print(n1)
else:
    print(n2)    
