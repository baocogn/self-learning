def change(x):
    if 'a' <= x <= 'z':
        return ord(x) - ord('a')
    else:
        return ord(x) - ord('A') + 26

ans = "null"
count = [0]*52
s = input()
for i in s:
    Ord = change(i)
    count[Ord] += 1
    if count[Ord] == 2:
        ans = i
        break
print(ans)
