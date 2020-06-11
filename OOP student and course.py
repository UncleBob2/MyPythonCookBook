class Student:
        def __init__(self, name, age,grade):
            self.name = name
            self.age = age
            self.grade = grade

        def get_grade(self):
            return self.grade

class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []  # creating an attribute but it is not assigned

    def get_grade(selfs):
        return self.grade

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("Student was added to course: ",student.name)
        else: print("Student was not added: ", student.name)

    def students_in_course(self):
        for student in self.students:
            print(student.name)

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

    def __str__(self,student):
        return student.name




s1 = Student("Tim", 19, 93)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

course.students_in_course()
print(course.get_average_grade())






