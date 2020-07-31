"""Program Plan:

* Create a function printintro() to inform the user about the simulaiic-r..

+ Create a function getinput() to ask the user for the number of darts to be thrown, which is the
simulation parameter.

* Create a function findPi(n) which simulates darts n times and count the times when the dart hit
the circle. The function should return the number of time the dart hit the board and the calculated
value of pi.

* Create a function isOnTheDartBoard(} to check if the dart has hit the dart. This function is to be
used by findPi().

* Create a function generateCoordinate() to randomly generate X and Y coordinate. This function
is required by isOnTheDartBoara() for simulation of darts.

* Create a function printSummary() to print the value of pi."""

# Get the input from the user and assign it to variable

import random


def main():
    # printIntro()
    n = getinput()
    count, pi = findPi(n)  # returning 2 variable while exporting 1 variable
    # Call the printSummary method which takes three values as an arguments.
    printSummary(count, n, pi)


def printintro():
    # prints and introduction to the simulation.
    print("This program simulates playing darts")
    print("to estimate the value of pi")


def getinput():
    """This function is created to ask the user for the number of darts which is the simulation parameter"""
    n = eval(input("Number of darts? "))
    return n


def generateCoordinate():
    """This function used the random() function to co-ordinate between -0.5 to 0.5 as the origin is
    assumed to be the center of the square."""
    # return 2 * random() - 1
    return random.uniform(0.00001, 1.00001)


def isOnTheDartBoard():
    """Based on the co-ordinates generated and the equation of the circle, this function checks if the
    dart falls on the board"""
    xCoord = generateCoordinate()
    yCoord = generateCoordinate()
    # checks if the co-ordinates fall in the circle
    if ((xCoord ** 2) + (yCoord ** 2)) < 1:
        return True  # inside the circle - area of circle = piR^2 = pi(0.5)(0.5)
    else:
        return False  # outside of the cirle but still inside the 1 x 1 square  = 1


def findPi(n):
    """This is the main simulation function. It counts the number of times a dart hits the dartboard.
    Based on the number, the value of pi is calculated."""
    # Simulates a dart game n times
    # Calculates the number of times a
    # dart hits the board
    # Area of square = 1, Area of circle of Pi(0.25)
    # n throws contains both inside the
    # pi = 4*(inside circle)/ n throws
    count = 0
    for i in range(n):
        if isOnTheDartBoard() == True:
            count += 1
    return count, (4.00 * float(count) / float(n))


def printSummary(count, n, pi):
    """Prints the value of pi"""
    print("\nNumber of times dart game is played:{0}".format(n))
    print("Number of times it hit the dart: {0}".format(count))
    print("Value of pi: ", pi)


# Call the main method

if __name__ == "__main__":
    main()

# number of times:3,684,692
# number of hit:
# value of pi: 3.1415

