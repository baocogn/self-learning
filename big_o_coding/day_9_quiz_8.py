n = int(input())

cached = {}
def f(n):
    if n in cached:
        return cached[n]
    if 0 <= n <= 1:
        return 1
    f_n = f(n-1) + f(n-2) 
    cached[n] = f_n
    return f_n
    
print(f(n))