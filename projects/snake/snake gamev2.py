#snake_OOP Tutorial Python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

pygame.init()

class cube(object):
    #global width, rows, height, columns, snake, snack
    width = 500 # width of our screen
    height = 500 # height of our screen
    rows = 20 # amount of rows
    columns = 20 # amount of columns

    def __init__(self,start, x_axis=1,y_axis=0,color=(255,0,0)):
        self.position = start
        self.x_axis = 1
        self.y_axis = 0
        self.color = color


    def move(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.position = (self.position[0] + self.x_axis, self.position[1] + self.y_axis)

    def draw(self, backGround, eyes=False):
        #gridWidth = width//columns # Gives us the distance between the lines
        #gridHeight = height // rows

        cube_height = self.height // self.rows
        cube_width = self.width//columns

        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(backGround, self.color, (i*cube_width+1,j*cube_height+1, cube_width-1, cube_height-1))

        if eyes:
            centre = cube_height//2
            radius = 3
            circleMiddle = (i*cube_height+centre-radius,j*cube_height+8)
            circleMiddle2 = (i*cube_height + cube_height -radius*2, j*cube_height+8)
            pygame.draw.circle(backGround, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(backGround, (0,0,0), circleMiddle2, radius)




class snake_OOP(object):
    pygame.init()
    body = []
    turns = {}
    def __init__(self, position,color):
        self.color = color
        self.head = cube(position)
        self.body.append(self.head)
        self.x_axis = 0
        self.y_axis = 1

    def move(self):
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.x_axis = -1
                    self.y_axis = 0
                    self.turns[self.head.position[:]] = [self.x_axis, self.y_axis]

                elif keys[pygame.K_RIGHT]:
                    self.x_axis = 1
                    self.y_axis = 0
                    self.turns[self.head.position[:]] = [self.x_axis, self.y_axis]

                elif keys[pygame.K_UP]:
                    self.x_axis = 0
                    self.y_axis = -1
                    self.turns[self.head.position[:]] = [self.x_axis, self.y_axis]

                elif keys[pygame.K_DOWN]:
                    self.x_axis = 0
                    self.y_axis = 1
                    self.turns[self.head.position[:]] = [self.x_axis, self.y_axis]

                elif keys[pygame.K_q]:
                    pygame.quit()


        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.x_axis == -1 and c.position[0] <= 0: c.position = (c.rows-1, c.position[1])
                elif c.x_axis == 1 and c.position[0] >= c.rows-1: c.position = (0,c.position[1])
                elif c.y_axis == 1 and c.position[1] >= c.rows-1: c.position = (c.position[0], 0)
                elif c.y_axis == -1 and c.position[1] <= 0: c.position = (c.position[0],c.rows-1)
                else: c.move(c.x_axis,c.y_axis)


    def reset(self, position):
        self.head = cube(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.x_axis = 0
        self.y_axis = 1


    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.x_axis, tail.y_axis

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.position[0]-1,tail.position[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.position[0]+1,tail.position[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.position[0],tail.position[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.position[0],tail.position[1]+1)))

        self.body[-1].x_axis = dx
        self.body[-1].y_axis = dy


    def draw(self, backGround):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(backGround, True)
            else:
                c.draw(backGround)


def drawGrid(width, rows, height,columns, backGround):
    gridWidth = width//columns # Gives us the distance between the lines
    gridHeight = height // rows
    x,y = 0,0

    for column in range(columns):
        x = x + gridWidth
        pygame.draw.line(backGround, (0,255,255), (x,0),(x,height)) # vertical lines

    for row in range(rows):
        y = y + gridHeight
        pygame.draw.line(backGround, (0,255,255), (0,y),(width,y)) # horizontal lines



def redrawWindow(backGround):
    global rows, width, height, columns, snake, snack
    backGround.fill((100,100,100))
    snake.draw(backGround)
    snack.draw(backGround)
    drawGrid(width,rows, height, columns, backGround)
    pygame.display.update()


def randomSnack(rows,columns, item):

    positionitions = item.body

    width = 500 # width of our screen
    height = 500 # height of our screen
    rows = 20 # amount of rows
    columns = 20 # amount of columns
    cube_height = height // rows
    cube_width = width//columns

    centre = cube_height//2
    radius = 3
    circleMiddle = (i*cube_height+centre-radius,j*cube_height+8)
    circleMiddle2 = (i*cube_height + cube_height -radius*2, j*cube_height+8)
    pygame.draw.circle(backGround, (0,0,0), circleMiddle, radius)
    pygame.draw.circle(backGround, (0,0,0), circleMiddle2, radius)

    while True:
        x = random.randrange(rows)
        y = random.randrange(columns)
        if len(list(filter(lambda z:z.position == (x,y), positionitions))) > 0:
            continue
        else:
            break

    return (x,y)




def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, height, columns, snake, snack
    width = 500 # width of our screen
    height = 500 # height of our screen
    rows = 20 # amount of rows
    columns = 20 # amount of columns
    screenSize= pygame.display.set_mode((width, height)) # using pygame to set display screen size
    snake = snake_OOP( (10,10), color=(255,0,0))  # position x,y  color =red,
    snack = cube(randomSnack(rows,columns, snake),color=(0,255,0)) #  position x,y, color = green,
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(120) ## This will delay the game so it doesn't run too quickly
        clock.tick(10) # Will ensure our game runs at 10 FPS
        snake.move()
        redrawWindow(screenSize)# This will refresh our screen

        if snake.body[0].position == snack.position:
            snake.addCube()
            snack = cube(randomSnack(rows, columns, snake), color=(0,255,0))

        for x in range(len(snake.body)):
            if snake.body[x].position in list(map(lambda z:z.position,snake.body[x+1:])):
                print('Score: ', len(snake.body))
                message_box('You Lost!', 'Play again...')
                snake.reset((10,10))
                break





main()
