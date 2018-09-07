def gcd(a, b):
    while b!= 0:
        r = a % b
        a = b
        b = r
    return a

class Fraction:
    def __init__(self, nu, de):
        self.nu = nu
        self.de = de

    def sumFraction(self, other):
        ans = Fraction(0, 1)
        ans.nu = self.nu * other.de + other.nu * self.de
        ans.de = self.de * other.de
        return ans
    
    def reduceFraction(self):
        x = gcd(abs(self.nu), abs(self.de))
        self.nu //= x
        self.de //= x

x, y = map(int, input().split(' '))
p1 = Fraction(x, y)
    
x, y = map(int, input().split(' '))
p2 = Fraction(x, y) 

p3 = p1.sumFraction(p2)
p3.reduceFraction()
print("{0} {1}".format(p3.nu, p3.de))