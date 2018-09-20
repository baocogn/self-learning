a, b = map(int, input(). split())

def GCD(a, b):
    res = 1
    for x in range (1, a + 1):
        if a % x == 0 and b % x == 0:
            res = x
    return res

c = a / GCD(a, b)
d = b / GCD(a, b)
print("{0} {1}".format(int(c), int(d)))