class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Bark! Bark!")

    def doginfo(self):
        print("{} is {} years old".format(self.name, self.age))

    def birthday(self):
        self.age += 1

    def buddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = buddy


ozzy = Dog("Ozzy", 2)

ozzy.bark()


ozzy.doginfo()

ozzy.birthday()

print(ozzy.age)

'jue' = ozzy.buddy()

print(ozzy.buddy())