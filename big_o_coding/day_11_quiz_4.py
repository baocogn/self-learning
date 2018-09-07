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


def merge(Left, Right):
    l, r = 0, 0
    results = []
    while l < len(Left) and r < len(Right):
        if Left[l] > Right[r]:
            results.append(Left[l])
            l += 1
        elif Left[l] <= Right[r]:
            results.append(Right[r])
            r += 1
    results.extend(Right[r:]) if r < len(Right) else results.extend(Left[l:])
    return results

def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))


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
