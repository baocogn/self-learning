# return ceil(a / b)
def ceil(a, b):
    r = a % b
    if r == 0:
        return a // b
    else:
        return a // b + 1
    

n, m, a = map(int, input().split())
height = ceil(n, a)
width = ceil(m, a)

print(height * width)