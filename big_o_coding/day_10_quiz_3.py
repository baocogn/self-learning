class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

x, y = map(int, input().split())
A = Point(x, y)

z, t = map(int, input().split())
B = Point(z, t)

ans = A.distance(B)
print("{0:.2f}".format(ans))