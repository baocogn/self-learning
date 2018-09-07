class Student:
    def __init__(self, id_number, math_score, literature_score):
        self.id_number = id_number
        self.math_score = math_score
        self.literature_score = literature_score

n, q = tuple(map(int, input().split()))
students = {}
for _ in range(n):
    raw_input = input().split(" ")
    id_number = str(raw_input[0])
    math = float(raw_input[1])
    literature = float(raw_input[2])

    students[id_number] = Student(id_number, math, literature)

for _ in range(q):
    id_number = input()
    print("{0:.2f} {1:.2f}".format(
        students[id_number].math_score,
        students[id_number].literature_score
    ))
