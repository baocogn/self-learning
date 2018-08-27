n = int(input())

def f(n):
    if 0 <= n <= 1:
        return 1
    return f(n-1) + f(n-2) 
    
print(f(n))