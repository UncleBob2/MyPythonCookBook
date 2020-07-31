"""Program Plan:

* Create a function printintro() to introduce the users to the game.
* Create a function printRules() to list down the game rules.
* Create a function getinput() to ask the user for the number of games to be simulated.
* Create a function simNGames() which simulates multiple games of Craps.
* Create a function simOneGame() which implements all the rules of the game and returns
whether the player has one the game. This function requires generating random integers in the
range 1 to 6, both inclusive, to simulate the roll of two dices. Create a function rollTwoDices() for
this.

* Create a function checkifWon() to be used by simOneGame(). This function implements all the
rules of the game and returns if the game has been won or lost.
* Create a function printSummary() which prints the final statistics of the simulation."""

from random import randrange


def main():
    # printintro()
    # printRules()
    n = getInputs()
    wins = simNGames(n)
    print("wins from 500 sim", wins)
    printSummary(wins, 500)


def printintro():
    """prints and introduction to the game."""
    print("This program simulates n games of")
    print("Craps' which is a dice based game.")


def printRules():
    """Informs the user about the basic rules of the game."""
    print("\nThe rules of the game are:")
    print("1. Roll a pair of normal six-faced dice.")
    print("2. If the initial roll is 2, 3 or 12 — the player loses")
    print("3. If the roll is 7 or 11 — the player wins")
    print("4. Any other roll leads to roll for point.")
    print("5. The player continues to roll till he gets")
    print(" a 7 of re-rolls the previous value.")
    print("6. The player loses by rolling a 7 while")
    print("re-rolling the same value allows the playerto wins.\n")


def getInputs():
    # Returns the three simulation parameters probA, probB and n
    n = eval(input("How many games to simulate? "))
    return n


def simNGames(n):
    wins = 0
    for i in range(n):

        won = simOneGame()
        print(i, won)
        # checking the condition whether won is true or not.
        if won is True:
            print("wins = ", wins)
            # increment the value of wins with 1.
            wins += 1
    return wins


# The function calls rollTwoDices() which gives the sum of values on two normal dices. It calls
# checkifWon() with the dice value as a parameter.


def simOneGame():
    # Simulates a single game of Craps
    # Returns whether the game was won or lost
    sumDice = rollTwoDices()
    # print("True=Win, False=loss  ", checkIfWon(sumDice))
    return checkIfWon(sumDice)


def rollTwoDices():
    """This function uses randrange() to generate a number between 1 and 6 and returns the sum of
    two such values."""
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)
    # returns the sum of dice values
    sumDice = dice1 + dice2
    return sumDice


# This function implements all the rules with respect to the value on the dices.
def checkIfWon(sumDice):
    # checks if the player has won or lost
    # This function implements all the rules of the game
    if sumDice == 2 or sumDice == 3 or sumDice == 12:
        return False
    elif sumDice == 7 or sumDice == 11:
        return True
    else:
        while True:
            additionalRoll = rollTwoDices()
            print("additionalRoll", additionalRoll)
            if additionalRoll == sumDice:
                return True
            elif additionalRoll == 7:
                return False


def printSummary(wins, Sim):
    print("\nGames simulated: {0}".format(Sim))
    xSim = wins / Sim
    print("Wins for the player: {0} ({1:.2%})".format(wins, xSim))


if __name__ == "__main__":
    main()
