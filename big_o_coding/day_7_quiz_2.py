a = str(input())

count = 0
for i in range(len(a)):
    s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for j in s:
        if j in a[i]:
            count += 1
    
print(count)