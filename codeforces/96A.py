string = input()

def f(s):
    t1, t2 = '0000000', '1111111'
    if t1 in s or t2 in s:
        return "YES"
    else:
        t1 += '0'
        t2 += '1'
    return "NO"

print(f(string))