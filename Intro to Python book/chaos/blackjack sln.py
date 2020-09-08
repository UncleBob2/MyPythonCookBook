from random import randrange


def main():
    #n = getinputs()
    #busts = simNGames(n)
    #printSummary(busts, n)
    print(simOneGame())


def getinputs():
    n = eval(input("How many games do you want to simulate ?"))
    return n


def simNGames(n):
    bustsDealer = 0
    for i in range(n):
        # Call the simOneGame method
        bust = simOneGame()
    # Check the condition till bust is True
        if bust is True:
            # Increase the value of bustsDealer with 1.
            bustsDealer = bustsDealer + 1
    return bustsDealer


x = []


def simOneGame():
    valueDealer = 0
    valuePlayer = 0
    hasAce = False
    # Check the condition using the while loop till the value of valueDealer is less than 17.
    while valueDealer < 17:
        # The dealer starts the game
        value = findCardValue()
        x.append(value)
    # Add the value of the card
        valueDealer = valueDealer + value
    # Check the condition when value is equal is 1.
        if value == 1:
            hasAce = True
    # If you have an ace, you can use it as 11
    # if it satisfies the below mentioned condition
        if hasAce == True and valueDealer >= 7 and valueDealer <= 11:
            valueDealer = valueDealer + 10
        # If the value for dealer increases 21, the dealer
        # busts
        print(x)
        print(valueDealer)
        if valueDealer > 21:
            return True

    # It is now player's turn

    value = findCardValue()
    valuePlayer = valuePlayer + value
    # The player busts in this case
    if valuePlayer > 21:
        return False

    # Reaching here means that the dealer has a value
    # above 17 and didn't bust

    return False


def findCardValue():
    # This functions simulate getting a card
    # It retums a value associated with
    # the card that is relevant to the game
    card = randrange(1, 13)
    if card >= 10:
        return 10
    else:
        return card
    # This function prints the summary and the calculated probability of a dealer busting a game.


def printSummary(busts, nSim):
    # Prints a summary of busts for the dealer
    print("\nGames simulated: {0}".format(nSim))
    nSim = float(nSim)
    print("Busts for the dealer: {0} ".format(busts))
    print("Probability of dealer busting: " '%.4f' % (busts/nSim))


# Call the main function
if __name__ == '__main__':
    main()
