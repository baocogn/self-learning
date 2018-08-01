highest = -1
lowest = 11
while(True):
    x = int(input())
    if x == -1:
        break
    if x > highest:
        highest = x
    if x < lowest:
        lowest = x

print(highest, lowest)    
    