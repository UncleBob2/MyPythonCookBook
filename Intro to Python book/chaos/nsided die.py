# msdie.py
# Class definition for an n-sided die.
from random import randrange


class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


def main():
    print("executing code")
    die1 = MSDie(13)
    die1.roll()
    print(die1.getValue())


main()
