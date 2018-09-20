s = input()

flag = True
ans1 = 0
ans2 = -1
for i in range(len(s)):
    if ord(s[ans1]) != ord(s[ans2]):
        flag = False
    else:
        ans1 += 1
        ans2 -= 1
        
if flag == True:
    print("YES")
else:
    print("NO")