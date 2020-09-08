from random import randrange


class Cards:
    def __init__(self, rank, suit):
        # getRank()
        self.rank = rank
        # value for card representing J,Q,K assigned as ten
        if self.rank > 10:
            self.value = 10
        else:
            # equal to self.rank
            self.value = self.rank

        # define full name for suit
        if suit == 1:
            self.suit = 'Diamonds'
        elif suit == 2:
            self.suit = 'Clubs'
        elif suit == 3:
            self.suit = 'Hearts'
        elif suit == 4:
            self.suit = 'Spades'

        # define cards' real value
        if self.rank == 1:
            self.n_Name = 'Ace'
        elif self.rank == 2:
            self.n_Name = 'Two'
        elif self.rank == 3:
            self.n_Name = 'Three'
        elif self.rank == 4:
            self.n_Name = 'Four'
        elif self.rank == 5:
            self.n_Name = 'Five'
        elif self.rank == 6:
            self.n_Name = 'Six'
        elif self.rank == 7:
            self.n_Name = 'Seven'
        elif self.rank == 8:
            self.n_Name = 'Eight'
        elif self.rank == 9:
            self.n_Name = 'Nine'
        elif self.rank == 10:
            self.n_Name = 'Ten'
        elif self.rank == 11:
            self.n_Name = 'Jack'
        elif self.rank == 12:
            self.n_Name = 'Queen'
        elif self.rank == 13:
            self.n_Name = 'King'

    # Define a method __str__Qwhich will return the name of a card.
    def __str__(self):
        return self.n_Name+' of ' + self.suit

    # Define a method BJvalue(jwhich will return a black jack value of a card.
    def BJvalue(self):
        return self.value

    # Define a method getRank(Qwhich will return a rank of cards.
    def getRank(self):
        return self.rank

    # Define a method getSuit()which will retum suit of a card.
    def getSuit(self):
        return self.suit


def main():
    # print_Intro()
    n, test1 = get_Input()
    print(n, test1)
    if test1 != 'error':
        for i in range(n):
            card = draw_Card()
            print_CardInfo(i, card)


def get_Input():
    n = test1 = 0
    try:
        n = eval(input('How many cards are needed for draw?'))
        print()
    except ValueError:
        print('\nError! interger numbers are only acceptable.')
        test1 = 'error'
    except NameError:
        print('Error! integer numbers are only acceptable.')
        test1 = 'error'
    except:
        print('Unknown error!')
        test1 = 'error'
        # second check to be done for minus number input
    if test1 != 'error':
        n, test1 = verify_Input(n, test1)
    return n, test1


def verify_Input(n, test1):
    if n <= 0:
        test1 = 'error'
        print('Error!. positive integer number are required.')
    return n, test1


def draw_Card():
    rank, suit = gen_CardValue()
    ca = Cards(rank, suit)
    return ca


def gen_CardValue():
    card = randrange(1, 14)
    suite = randrange(1, 5)
    return card, suite


def print_CardInfo(i, card):
    print('Card', i+1, ' is ', card, 'having value of', card.BJvalue())


if __name__ == '__main__':
    main()
