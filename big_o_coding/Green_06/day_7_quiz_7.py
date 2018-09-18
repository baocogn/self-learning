a = input()

res = ""
needaSpace = False
needUpper = False

for char in a:
    if char == ".":
        needaSpace = True
        res += " "
    elif char != ".":
        
    