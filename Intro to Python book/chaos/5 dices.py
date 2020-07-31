import random

count = 0
# for i in range(100_000):
# d1 = random.randrange(1, 7)
# d2 = random.randrange(1, 7)
# d3 = random.randrange(1, 7)
# d4 = random.randrange(1, 7)
# d5 = random.randrange(1, 7)
# if d1 == d2 == d3 == d4 == d5:
#     jackpot += 1
def isFiveofKind():
    d1 = rollDice()
    for i in range(4):
        d2 = rollDice()
        # print(d1, d2)
        if d1 != d2:
            return False
        d1 = d2
    print("any luck here")
    return True


# print("percent of jackpot {0} {1:.5%}".format(jackpot, jackpot / 100_000))


def rollDice():
    d1 = random.randrange(1, 7)
    return d1


for i in range(100_000):
    jackpot = isFiveofKind()
    if jackpot == True:
        count += 1

print("percent of jackpot {0} {1:.5%}".format(count, count / 100_000))
