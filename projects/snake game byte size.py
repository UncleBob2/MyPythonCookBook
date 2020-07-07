import pygame as pg
import random
import time

# Colors
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
brown = pg.Color(165, 42, 42)
# Variables
screen_width = 400
screen_height = 400

# Initialize pygame
pg.init()
# The screen, pygame The origin (0,0) is located at the top left corner.
# upper right (screen_width,0), lower right corner (screen_width, screen_height)
wn = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('A simple game of Snake')


# The class for food object
class Food():
    # Initialization
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 4
        self.color = red
        self.width = 10
        self.height = 10

    # Makes the food visible

    def draw_food(self, surface):
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, self.color, self.food)

    # Is the food eaten?
    # e use a pygame inbuilt function that checks if two rectangles collide (this is the reason that food and the snakehead are initialized as py.Rect objects). If the two rectangles collide (snakehead and food), it returns ‘True’ else it returns ‘False.’

    def is_eaten(self, head):
        return self.food.colliderect(head)
    # Returns a new position for the food after it is eaten

    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

# The snake object


class Player():
    # Initialization
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.width = 10
        self.height = 10
        self.velocity = 10
        self.direction = 'stop'
        self.body = []
        self.head_color = green
        self.body_color = brown
    # Draws the snake on the given surface

    def draw_player(self, surface):
        self.seg = []
        self.head = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, self.head_color, self.head)
        if len(self.body) > 0:
            for unit in self.body:
                segment = pg.Rect(unit[0], unit[1], self.width, self.height)
                pg.draw.rect(surface, self.body_color, segment)
                self.seg.append(segment)
    # Increases length of snake

    def add_unit(self):
        if len(self.body) != 0:
            index = len(self.body) - 1
            x = self.body[index][0]
            y = self.body[index][1]
            self.body.append([x, y])
        else:
            self.body.append([1000, 1000])
    # Checks if there is any collision

    def is_collision(self):
        # Collision with itself
        for segment in self.seg:
            if self.head.colliderect(segment):
                return True
        # Collision with the boundaries
        if self.y < 0 or self.y > screen_height - self.height or self.x < 0 or self.x > screen_width - self.width:
            return True
    # Moves the snake in the direction of head

    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            x = self.body[index - 1][0]
            y = self.body[index - 1][1]
            self.body[index] = [x, y]
        if len(self.body) > 0:
            self.body[0] = [self.x, self.y]
        if self.direction == 'up':
            self.y -= self.velocity
        if self.direction == 'down':
            self.y += self.velocity
        if self.direction == 'left':
            self.x -= self.velocity
        if self.direction == 'right':
            self.x += self.velocity
    # Changes direction of head

    def change_direction(self, direction):
        if self.direction != 'down' and direction == 'up':
            self.direction = 'up'
        if self.direction != 'right' and direction == 'left':
            self.direction = 'left'
        if self.direction != 'up' and direction == 'down':
            self.direction = 'down'
        if self.direction != 'left' and direction == 'right':
            self.direction = 'right'


score, high_score = (0, 0)
# Draw the score on the screen


def draw_score(surface):
    global high_score  # declare global to access and modify the high score variable
    font_name = pg.font.match_font('arial')  # choose font with arial in it
    if score > high_score:  # set high score as current score if it is higher than current score
        high_score = score
    # writing the score
    font = pg.font.Font(font_name, 18)
    # The next three lines create a rectangle to display the score
    text_surface = font.render(
        'Score: {} High Score: {}'.format(score, high_score), True, white)

    # Next, we get the rectangle on which the text is drawn via get_rect() and place its mid-top position at (200,10) in the next line. The final line writes the score in the text_rect object.
    text_rect = text_surface.get_rect()
    text_rect.midtop = (200, 10)
    surface.blit(text_surface, text_rect)


# What to do when the game is over
# The function first writes the word “Game Over” on the screen (the first 6–7 lines). Then it resets the score to 0. pg.display.flip() is used to update the screen so that the changes made above are visible. Next, we call the time.sleep() function from the time module, which makes the screen unresponsive for 2 seconds. Finally, we re-initialize the whole game by creating new food and player objects and initializing the game environment using the play_game function.
def game_over():
    global score
    # writing game over
    gameOverFont = pg.font.Font('freesansbold.ttf', 24)
    gameOverSurf = gameOverFont.render('Game Over', True, white)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (200, 50)
    wn.blit(gameOverSurf, gameOverRect)
    # reset score
    score = 0
    pg.display.flip()
    time.sleep(2)
    # re-initialize game
    run = True
    fd = Food()
    p = Player()
    play_game(fd, p)


# The game
# The play_game function takes the two objects (food and player) as the input and makes them play the game.
def play_game(fd, p):
    global score
    run = True
    while run:
        # FPS
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        # draw food, snake, score
        wn.fill(black)
        fd.draw_food(wn)
        p.draw_player(wn)
        draw_score(wn)
        # user input
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            p.change_direction('up')
        if pressed[pg.K_LEFT]:
            p.change_direction('left')
        if pressed[pg.K_DOWN]:
            p.change_direction('down')
        if pressed[pg.K_RIGHT]:
            p.change_direction('right')
        # move snake
        p.move()
        # eating
        if fd.is_eaten(p.head):
            fd.new_pos()
            p.add_unit()
            score += 10
        # collision
        if p.is_collision():
            run = False
            game_over()


pg.display.update()


# The mainloop
run = True
while run:
    # Catches all the events that have happened since the game started
    for event in pg.event.get():
        # When you press the close window button
        if event.type == pg.QUIT:
            run = False
    # Fills the screen with black color
    wn.fill(black)
    fd = Food()
    p = Player()
    play_game(fd, p)
# Exits pygame
pg.quit()
