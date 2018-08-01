hprev = -1
flag = True
while(True):
    hcur = int(input())
    if hcur == 0:
        break
    elif hcur < hprev:
        flag = False
    hprev = hcur
        
if flag == True:
    print("YES")
elif flag == False:
    print("NO")

