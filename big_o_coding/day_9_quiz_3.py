n = int(input())

def c(n):
    if n >= 10:
        return 1 + c(n // 10)
    return 1

if n < 0:
    n = -n
    
print(c(n))