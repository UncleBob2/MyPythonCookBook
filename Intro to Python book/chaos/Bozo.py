class Bozo:
    def __init__(self, value):
        print("Creating a Bozo from: ", value)
        self.value = 2 * value

    def clown(self, x):
        print("Clowing:", x)
        print("x*self", x * self.value)
        return x + self.value


def main():
    print("Clowing around now.")
    c1 = Bozo(3)
    c2 = Bozo(4)

    print(c1.clown(3))
    print(c2.clown(c1.clown(2)))


# http://www.pythontutor.com/visualize.html#mode=display
main()
