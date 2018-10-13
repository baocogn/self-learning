import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

class Triangle:
    def __init__(self, a, b, c):
        self.point_a = a
        self.point_b = b
        self.point_c = c

    def p(self):
        ab = self.point_a.distance(self.point_b)
        bc = self.point_b.distance(self.point_c)
        ca = self.point_c.distance(self.point_a)
        
        return ab + bc + ca
    
    def s(self):
        ab = self.point_a.distance(self.point_b)
        bc = self.point_b.distance(self.point_c)
        ca = self.point_c.distance(self.point_a)

        half_p = (ab + bc + ca) / 2
        area = (half_p * (half_p - ab) * (half_p - bc) * (half_p - ca)) ** 0.5

        return area
    
    def g(self):
        x_g = (self.point_a.x + self.point_b.x + self.point_c.x) / 3
        y_g = (self.point_a.y + self.point_b.y + self.point_c.y) / 3
        return x_g, y_g


points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append(Point(x, y))

triangle = Triangle(points[0], points[1], points[2])
print("{0:.2f}".format(triangle.p()))
print("{0:.2f}".format(triangle.s()))
x, y = triangle.g()
print("{0:.2f} {1:.2f}".format(x, y))
