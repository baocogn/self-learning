s = list(input())

min_x = '99'
res = ""
for i in range(len(s)):
    if ord(s[i]) < ord(min_x):
        min_x = s[i]
    res = res + s[i]

print(res)