
n = int(input())
result = 1
for i in range(1, n + 1):
    result = i * result
    result = result % 1000003

print(result)

