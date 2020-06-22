import random

def randomWalkLength(n):
    '''Return coordinates after 'n' block of a random walk'''
    x,y = 0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x+=dx
        y+=dy
    return(x,y)


numberOfWalk = 100000

for walk_length in range(1,31):
    no_transport = 0 #Number of walks with 4 or fewer blocks from home
    for i in range(numberOfWalk):
        (x,y) = randomWalkLength(walk_length)
        distance = abs(x) + abs(y)
        if distance <=4:
            no_transport +=1
    no_transport_percentage = float(no_transport) / numberOfWalk
    print("Walk size = ", walk_length, " /% of no transport = ", 100*no_transport_percentage)
