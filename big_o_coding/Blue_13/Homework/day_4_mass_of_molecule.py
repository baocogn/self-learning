s = input()

stack = []
for i in range(0, len(s)):
    if s[i] == "C" or s[i] == "H" or s[i] == "O":
        stack.append(s[i])
    elif s[i] == "(":
        stack.append(-1)
    elif s[i] == ")":
        w = 0
        for x in stack:
            while x != -1:
                stack.pop()
                