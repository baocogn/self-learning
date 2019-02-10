k, n, w = map(int, input().split())
res = 0
price = 0

for i in range(1, w+1):
    price += i*k
if n < price:
    res = price - n
else:
    res = 0

print(res)
