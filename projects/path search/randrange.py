import random
BOARD_SIZE=(48,48)

position = tuple(random.randrange(BOARD_SIZE[i]) for i in (0,1))
print(position)
