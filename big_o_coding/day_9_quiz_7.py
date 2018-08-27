n = int(input())
numbers = list(map(int, input().split()))[:n]

#check if x is prime:
def recursive_is_prime(x, checker):
    if x <= 1: return False
    if x <= 3: return True
    if x % checker == 0:
        return False
    if checker > int(x**0.5) + 1:
        return True
    return recursive_is_prime(x, checker + 1)

#function to check isprime:
def is_prime(x):
    if x <= 1: return False
    if x <= 3: return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def first_prime(l):
    for i in range(len(l)):
        if recursive_is_prime(l[i], 2):
            return i
    return -1

print(first_prime(numbers))