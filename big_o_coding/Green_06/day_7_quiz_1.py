n = int(input())

for i in range(n):
    m = str(input())
    s = ['B', 'b', 'I', 'i', 'O', 'o', 'G', 'g']
    flag = False
    for i in range(len(s)):
        if s[i] in m:
            flag = True

    if flag == True:
        print("YES")
    else:
        print("NO")

    
