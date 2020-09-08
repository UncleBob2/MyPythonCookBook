import random

adjectives = """ bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy foolish foul gross heedless indistinguishable infected insatiate irksome lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced toad-spotted unmannered vile wall-eyed
""".strip().split()

nouns = """ Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
gull harpy jack jolthead knave liar lunatic maw milksop minion ratcatcher recreant rogue scold slave swine traitor varlet villain worm """.strip().split()
# print(adjectives)
# print(nouns)
for _ in range(random.randint(1, 3)):
    adjs = ", ".join(random.sample(adjectives, k=random.randint(1, 5)))
    print(f"You {adjs} {random.choice(nouns)}!")

