import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []  # create a list of 52 cards (variable)
        self.build()  # func

    def build(self):
        for suit in ["Spaces", "Club", "Hearts", "Diamonds"]:
            for value in [
                "Ace",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "Jack",
                "Queen",
                "King",
            ]:
                self.cards.append(Card(value, suit))

    def show(self):
        for index in self.cards:
            index.show()

    def shuffle(self):
        """We want to go from the end of our list back to the beginning. We create a for loop in our method, for “i in (range(len(self.cards)) minus 1 (which is the last element and in this case we want to go to zero), 0, -1 decrement)”. If we run the loop we get values 51–1 which is what we want because when we are accessing elements in an array, we want to start with the length minus 1 because the index starts at 0. In this case we want to start at 1 because by the time we shuffle every other card, that 0 index is also going to be shuffled and we don’t want to shuffle that one itself."""
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        x = self.hand
        print(x)
        for card in x:
            card.show()


deck = Deck()
deck.shuffle()

bob = Player("Bob")
for i in range(5):
    bob.draw(deck)

bob.showHand()

