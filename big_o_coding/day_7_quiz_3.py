a = input()

res = ""
resLen = 0
needASpace = False

for char in a:
    if char == " ":
        if resLen > 0 and res[-1] != " ":
            needASpace = True
    elif char != " ":
        if needASpace == True:
            res = res + " " + char
            resLen += 2
            needASpace = False
        else:
            res += char
            resLen += 1
        
print(res)        