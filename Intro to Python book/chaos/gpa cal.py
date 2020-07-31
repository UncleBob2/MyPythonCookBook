class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    # def name(self):
    #     return self.name

    # def hours(self):
    #     return self.hours

    # def qpoints(self):
    #     return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours


BestStudent = Student(" ", 1, 1)
firstStudent = Student(" ", 1, 1)

with open(
    "/Users/winsorhoang/dev/python/Intro to Python book/chaos/student.txt", "r"
) as f:
    for line in f:
        a = line.split("\t")
        # print(a)
        firstStudent = Student(a[0], float(a[1]), float(a[2]))
        # print(
        #     firstStudent.name,
        #     firstStudent.hours,
        #     firstStudent.qpoints,
        #     firstStudent.gpa(),
        # )
        if firstStudent.gpa() > BestStudent.gpa():
            BestStudent = firstStudent

print(
    "Best Student Name: ",
    BestStudent.name,
    "\n",
    "Hours: ",
    BestStudent.hours,
    "\n",
    "Quality Point: ",
    BestStudent.qpoints,
    "\n",
    "GPA: ",
    BestStudent.gpa(),
)
