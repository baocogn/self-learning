def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
n1 = n
n2 = n

while True:
    if isPrime(n1):
        break
    else:
        n1 -= 1

while True:
    if isPrime(n2):
        break
    else: 
        n2 += 1

if n - n1 <= n2 - n:
    print(n1)
else:
    print(n2)
            