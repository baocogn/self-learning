n = int(input())

def process(s):
    if len(s) > 10:
        result = s[0] + str(len(s) - 2) + s[-1]
    else:
        result = s
    return result

for i in range(n):
    s = input()
    print(process(s))
