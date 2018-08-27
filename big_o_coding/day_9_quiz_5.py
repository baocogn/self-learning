n = int(input())

def f(n):
    if n < 10:
        return n
    return max(f(n//10), n%10)

if n < 0:
    n = -n

print(f(n))    