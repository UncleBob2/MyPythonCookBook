import random
import os
from multiprocessing import Process, current_process

def randomWalkLength(n):
    '''Return coordinates after 'n' block of a random walk'''
    x,y = 0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x+=dx
        y+=dy
    return(x,y)

processes=[]
numberOfWalk = 100000

for walk_length in range(1,31):
    no_transport = 0 #Number of walks with 4 or fewer blocks from home
    for i in range(numberOfWalk):
        process = Process(target=randomWalkLength, args=(walk_length,))
        processes.append(process)
        process.start()
        #(x,y) = randomWalkLength(walk_length)
        
        distance = abs(process[0]) + abs(process[1])
        if distance <=4:
            no_transport +=1
    no_transport_percentage = float(no_transport) / numberOfWalk
    print("Walk size = ", walk_length, " /% of no transport = ", 100*no_transport_percentage)
