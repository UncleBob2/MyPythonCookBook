import random
import subprocess
subprocess.run('reset')


def getcard():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    x = random.randint(0, len(cards)-1)
    card1 = cards[x]
    return card1


def cal_val(num):
    sum = 0
    for i in range(len(num)):
        if num[i] == 'J' or num[i] == 'Q' or num[i] == 'K':
            num[i] = 10
        sum = sum + num[i]
    return sum


dealer_val = 0
player_val = 0
dealer_cards = []
has_ace = False

while dealer_val < 21:
    dealer_cards.append(getcard())
    dealer_val = cal_val(dealer_cards)
    if 1 in dealer_cards:
        has_ace = True
    if has_ace == True and dealer_val >= 7 and dealer_val <= 11:
        dealer_val = dealer_val + 10
    if dealer_val >= 17 and dealer_val <= 21:
        break
    if dealer_val > 21:
        print('Dealer bust')

print('Dealer Cards and value: ', dealer_cards, dealer_val)

# value = cal_val(player)
# if value > 21 and (11 in player):
#     print(value - 10)
# print('Value: ', value)
