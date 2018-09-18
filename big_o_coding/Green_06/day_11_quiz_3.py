n = int(input())
l = list(map(int, input().split()))[:n]

def merge(Left, Right):
    l, r = 0, 0
    results = []
    while l < len(Left) and r < len(Right):
        if Left[l] > Right[r]:
            results.append(Left[l])
            l += 1
        elif Left[l] <= Right[r]:
            results.append(Right[r])
            r += 1
    results.extend(Right[r:]) if r < len(Right) else results.extend(Left[l:])
    return results

def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))

def is_prime(x):
    if x <= 1: return False
    if x <= 3: return True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

is_primes = []
numbers = []
primes = []
for i in range(n):
    if is_prime(l[i]):
        is_primes.append(True)
        primes.append(l[i])
    else:
        is_primes.append(False)
        numbers.append(l[i])

numbers = list(reversed(merge_sort(numbers)))

results = []
number, prime = 0, 0
for i in range(n):
    if is_primes[i]:
        results.append(primes[prime])
        prime += 1
    else:
        results.append(numbers[number])
        number += 1

print(' '.join([str(x) for x in results]))
