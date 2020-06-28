import random

# random roll of a dice
for roll in range(10):
    value = random.randint(1, 6)
    print(value, end=', ')

greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
print()

value = random.choice(greetings)
print(value + ' , Coreys')

dice = [1, 2, 3, 4, 5, 6]
print(random.choices(dice, k=10))

colors = ['red', 'black', 'green']
print(random.choices(colors, weights=[18, 18, 2], k=10))

deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

hand = random.sample(deck, k=5)  # only want unique card
print(hand)
