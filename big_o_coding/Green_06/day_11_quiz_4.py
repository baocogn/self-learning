def average(x, y):
    r = (x + y) / 2
    return r

class Student:
    def __init__(self, name, id_number, math, literature):
        self.name = name
        self.id_number = id_number
        self.math = math
        self.literature = literature

    def average(self):
        self.score = average(self.math, self.literature)
        return self.score

    def less(self, other):
        if self.score < other.score:
            return True
        elif self.score == other.score and self.id_number < other.id_number:
            return True
        else:
            return False


def insertion_sort(n):
    for i in range(1, len(n)):
        x = n[i]
        j = i
        while (j > 0) and (n[j-1] > x):
            n[j] = n[j-1]
            j -= 1
        n[j] = x
    return n

n = int(input())

students = []
students_names = []
for _ in range(2):
    name = input()
    raw_input = input().split()
    id_number = raw_input[0]
    math = int(raw_input[1])
    literature = int(raw_input[2])

    students.append(raw_input)
    students_names.append(name)

l = list(zip(students, students_names))
l[name] = Student(name, id_number, math, literature)
