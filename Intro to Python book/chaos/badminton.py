"""
1) create a function printIntro() to print rules and info about the game
2) create a function getInputs() to ask users for each player's probability to win a rally
3) create a function simNGames() that simulates N games of badminton
4) create a function simOneGame() that simulates one game of badminton. This function would be called by simNGames(). Based on the scores returned by simOneGame(), simNGames() checks which player has won that game.
5) create a function gameOver() which returns true if one of the player has reached 21 points.
6) create a function printSummary() that prints the number of games won by both the players in simulation

"""
from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")


def getInputs():
    # Returns the three simulation parameters probA, probB and n
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n


def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # #abilities are represented by the probability of winning a serve.
    # # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB):
    scoreA = scoreB = 0
    serving = "A"
    # normProA = probA/(probA + probB)
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB += 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreB += 1

    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 21 or b == 21


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))


if __name__ == "__main__":
    main()
