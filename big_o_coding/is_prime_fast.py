import math

def is_prime(x):
    if x <= 1: return False
    if x <= 3: return True
    if x % 2 == 0: return False
    if x == 5: return True

    for i in range(5, int(math.sqrt(n)), 6):
        if x % i == 0:
            return False
    return True

n = int(input())
if is_prime(n):
    print("YES")
else:
    print("NO")
