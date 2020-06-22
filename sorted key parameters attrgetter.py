li = [-6,-5, -4,2,3, 5]
s_li = sorted(li, key=abs)
print (s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self): # represented func
        return '{}, {}, ${:,})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70_000)
e2 = Employee('Sarah',29, 80_000)
e3 = Employee('John', 43, 90_000)

# def e_sort(emp): #creating a sort function but better to use lambda since it is throw away
#     return emp.age # change age, name, salary

# employees = [e1,e2,e3]

# s_employees = sorted(employees, key=e_sort, reverse=True)
# print(s_employees)

from operator import attrgetter

employees = [e1,e2,e3]

#s_employees = sorted(employees, key=lambda e: e.salary, reverse=True)

s_employees = sorted(employees, key = attrgetter('age'))
print(s_employees)
