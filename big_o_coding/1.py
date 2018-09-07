class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5



class Rectangle:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def isRectangle(self):
        pass
    
    def p(self):
        ab = self.a.distance(self.b)
        ac = self.a.distance(self.c)
        bc = self.b.distance(self.c)
        cd = self.c.distance(self.d)
        
        return ab + ac + bc + cd

    def s(self):
        ab = self.a.distance(self.b)
        ac = self.a.distance(self.c)
        bc = self.b.distance(self.c)
        cd = self.c.distance(self.d)

        return 

    
        