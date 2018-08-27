n = int(input())

def f(n):
    if n >= 10:
        return f(n//10)
    return n

if n < 0:
    n = -n

print(f(n))