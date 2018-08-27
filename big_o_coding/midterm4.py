# first way:
n, m = map(int, input().split())

f_0 = 0 % m
f_1 = 1 % m
f_i = 1 % m

for i in range(2, n+1):
    f_i = (f_0 + f_1) % m
    f_0 = f_1 %  m
    f_1 = f_i % m

print(f_i % m)

# second way:
n, m = map(int, input().split())


