# Python Object Oriented Programming
# allow resuse logics and functions
# attributes and methods (function associated with class)
'''
class Employee:
    pass

emp_1 = Employee() #instance of employee class
emp_2 = Employee()
# instance variable vs class variable
# we don't want to manually set these variables every time for each employee
emp_1.first = "Corey"
emp_1.last = "Shafer"
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay    = 50000


emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = 'Test.User@company.com'
emp_2.pay    = 60000

print(emp_1) #<__main__.Employee object at 0x000002CBB2B3C4C0>
print(emp_2) #<__main__.Employee object at 0x000002CBB2BB6E20>
print(emp_1.email)
print(emp_2.email)
'''

string = "Hello"
print(string.upper()) #.upper is a method i.e. whenever you have a dot operator, the object here is string

class Employee:

    def __init__(self, first, last, pay):
        self.first = first  # attributues of the class
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self): #define a method within the class
        return '{} {}'.format(self.first, self.last) #use self to work with all instances


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname()) # the brackets are needed because fullname is a method, without the brackets then it is attribute

# The below two lines do the exact same thing
emp_1.fullname() #emp_1 is an instance, method does not need to pass in self
Employee.fullname(emp_1) # Employee is a class and the method is full name, we need to specify the instance

class Dog:
    # this method is initialized, name - whenever we create instance, we must give it a name
        def __init__(self, name, age, color):
            self.name = name  # name is an attribute of the class dog
            self.age = age
            self.color = color
            print("\nA new instance of class dog is created with name: ", name)

        def add_one(self,x):
            return x +1

        def bark(self):
            print("bark")

        def get_name(self):
            return self.name

        def get_age(self):
            return self.age

        def get_color(self):
            return self.color

        def set_age(self,age):
            self.age = age


d = Dog("Tim", 34,"red")  # Dog(), we are create an instance of class dog, "Tim" is an argument
d2 = Dog("Bill", 12, "brown")

print(d.name)
d.set_age(23)
print(d.age)
print(d.color)

print()
print(d2.get_name())
print(d2.get_age())
print(d2.get_color())


