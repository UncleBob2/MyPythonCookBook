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

print()
class Pet: # parent class
    number_of_pet = 0  # class attribute
    def __init__(self,name, age):
        self.name = name
        self.age = age
        Pet.number_of_pet +=1

    @classmethod
    def number_of_people(cls): # just act on the class and not the instance, not ref self
        return cls.number_of_people()

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old ")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):  # child class
    def speak(self):
        print('Meow')

class Dog(Pet):
    def __init__(self,name, age,color):
        super().__init__(name,age) # using super class
        self.color = color

    def speak(self):
        print("Bark")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Fish(Pet):
    pass

class Math:
    @staticmethod
    def add5(x):
        return x +5

    @staticmethod
    def add10(x):
        return x +10
    @staticmethod
    def pr():
        print('run')

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.speak()
print(Pet.number_of_pet)
d= Dog("Jill",25, "brown")
d.show()
f = Fish("Bubbles", 23)
f.speak()
print(Pet.number_of_pet)

Math.pr()




