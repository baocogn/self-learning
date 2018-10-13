lights = []
for i in range(4):
    light = list(map(int, input().split()))
    lights.append(light)

for i in range(0, 4):
    flag = True
    for j in range(0, 4):
        if lights[i][3] == 1 and (lights[i][2] == 1 or lights[i][1] == 1 or lights[i][0] == 1):
            flag = False
    
if flag == True:
    print("YES")
else:
    print("NO")
