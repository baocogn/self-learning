n = int(input())
a = list(map(int, input().split()))

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True

sum = 0
for k in range(len(a)):
    if isPrime(a[k]):
        sum = sum + 1

print(sum)
        
