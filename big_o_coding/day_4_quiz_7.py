s = input()

def palindrome(s):
    n = len(s)
    for i in range(int(n / 2)):
        if s[i] != s[n-1-i]:
            return False
    return True

if palindrome(s):
    print("YES")
else:
    print("NO")