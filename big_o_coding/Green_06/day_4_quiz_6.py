def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True

n = int(input())

s = 0
for y in range(0, n):
    if isPrime(y):
        s = s + y
        
print(s)
