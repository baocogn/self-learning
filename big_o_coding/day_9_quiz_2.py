n = int(input())

def f(n):
    if n % 2 != 0:
        return n
    return f(int(n/2))

print(f(n))   