from random import shuffle


class Card:
    def __init__(self, rank, suit):
        # rank lies in the range 1-13
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def findSuit(self):
        suit = self.suit
        if suit == "s":
            suit = "Spade"
        elif suit == "c":
            suit = "Clubs"
        elif suit == "h":
            suit = "hearts"
        elif suit == "d":
            suit = "Diamond"
        return suit

    def findRank(self):
        rank = self.rank
        if rank == 1:
            rank = "Ace"
        elif rank == 11:
            rank = "Jack"
        elif rank == 12:
            rank = "Queen"
        elif rank == 13:
            rank = "King"
        return rank

    def __str__(self):
        suit = self.findSuit()
        rank = self.findRank()
        return str(rank) + " of " + suit


class Deck:
    def __init__(self):
        self.deck = []
        self.count = 52
        # Use for loop to assign different suit and rank to card.
        for i in ["s", "c", "d", "h"]:
            for j in range(1, 14):
                card = Card(j, i)
                self.deck.append(card)

    def shuffleCards(self):
        shuffle(self.deck)

    def dealCard(self):
        # This function returns the card
        # which is on the top of deck
        # and removes that card
        card = self.deck[0]
        self.deck.pop(0)
        self.count = self.count - 1
        return card

    def cardsLeft(self):
        return self.count

    def printDeck(self):
        # This function prints the
        # complete deck
        for card in self.deck:
            print(card)


def main():
    deckOfCards = Deck()
    deckOfCards.shuffleCards()
    n = eval(input("How many cards you want to deal? "))
    print()
    for i in range(n):
        print(deckOfCards.dealCard())
    print("\nNo of Cards Left are " + str(deckOfCards.cardsLeft()))


if __name__ == "__main__":
    main()
