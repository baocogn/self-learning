class Employee:
    def __init__(self, id_number, name, yob):
        self.id_number = id_number
        self.name = name
        self.yob = yob
    
    def __eq__(self, other):
        return self.yob == other.yob and self.id_number == other.id_number

    def __lt__(self, other):
        return (self.yob < other.yob) or (self.yob == other.yob and self.id_number < other.id_number)
        
 
n = int(input())
min_employee = None
for _ in range(n):
    raw_input = input().split(" ")
    id_number = str(raw_input[0])
    name = str(raw_input[1])
    yob = int(raw_input[2])

    employee = Employee(id_number, name, yob)

    if min_employee is None:
        min_employee = employee
    elif employee < min_employee:
        min_employee = employee

print("{0} {1} {2}".format(
    min_employee.id_number,
    min_employee.name,
    min_employee.yob
))
