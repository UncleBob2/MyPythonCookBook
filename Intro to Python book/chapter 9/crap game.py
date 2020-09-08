import random
import subprocess
subprocess.run('reset')


def get_dice_val():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1, dice2, '\t', dice1+dice2)
    return (dice1 + dice2)


def singlegame():
    x = get_dice_val()
    value = x
    forPoint = 0
    if (value == 2 or value == 3 or value == 12):
        print('player loses')
        return(0)
    elif (value == 7 or value == 11):
        print('player wins')
        return(1)

    else:
        forPoint = value
        while True:
            value = get_dice_val()
            if value == 7:
                print('player loses')
                return(0)
            if value == forPoint:
                print('player wins')
                return(1)


win = 0
game = 10_000
for i in range(game+1):
    win += singlegame()
odd = float(win/float(game))
# ("{:.2f}".format(a))
print('\nProbability of winning: ', '{:.3f}'.format(odd))
