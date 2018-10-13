def average(x, y):
    r = (x + y) / 2
    return r

class Student:
    def __init__(self, name, math, literature):
        self.name = name
        self.math = math
        self.literature = literature
    
    def averagePoint(self):
        return average(self.math, self.literature)
        
s = input()
m, l = map(float, input().split())

point = Student(s, m, l)
print(s)
print("{0:.2f}".format(point.averagePoint()))
    