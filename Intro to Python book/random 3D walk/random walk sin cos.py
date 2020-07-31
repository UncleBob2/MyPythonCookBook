from random import random
import math
import matplotlib.pyplot as plt

# Define the main function as function call begins from here.
def main():
    path = []
    printintro()
    n = getinput()
    steps, path = walkRandomly(n)
    printSummary(steps, n)
    # print(path)
    x_val = [x[0] for x in path]
    y_val = [x[1] for x in path]
    plt.plot(x_val, y_val)
    plt.plot(x_val, y_val, "or")
    plt.show()


def printintro():

    # prints an introduction to the random walk.
    print("This program simulates a random walk")
    print("for n steps. The person can go a step")
    print("in any random direction ")
    print("with equal probability")


def getinput():
    n = eval(input("How many steps you want to walk? "))
    return n


# The concept of random direction is introduced here. At every point, a random angle is generated
# and the distance in X and Y directions are calculated.
def walkRandomly(n):

    distanceX = 0
    distanceY = 0
    x_axis, y_axis = 0, 0
    path = []
    # Iterate for loop in range n.
    for i in range(n):
        path.append(tuple((distanceX, distanceY)))
        angle = randomDirection()
        distanceX = distanceX + math.cos(angle)
        distanceY = distanceY + math.sin(angle)
        totalDistance = pow(distanceX, 2) + pow(distanceY, 2)
        totalDistance = pow(totalDistance, 0.5)
    return totalDistance, path


def randomDirection():
    # generates a random angle Uses the random() function to generate a random angle
    randomNo = random()
    angle = 2 * randomNo * math.pi
    return angle


# Prints the distance of the person from the origin
def printSummary(steps, n):
    # Prints a summary of the random walk
    print("\nTotal steps taken: {0}".format(n))
    print("Distance from start: {0}".format(steps))


# Call the main method
if __name__ == "__main__":
    main()

