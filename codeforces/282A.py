n = int(input())
x = 0

for i in range(n):
    s = input()
    t1 = '+'
    t2 = '-'
    if t1 in s:
        x += 1
    elif t2 in s:
        x -= 1

print(x)