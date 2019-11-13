import pygame
import math
import random
# -- Global Constants

# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640, 480)

screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")


# -- flip display to reveal new position of objects
# Create an address
# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#Classes & functions


class Ball():
    def __init__(self, x, y, x_dir, y_dir, col):
        self.color = col
        self.x_coord = x
        self.y_coord = y
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.size = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_coord, self.y_coord), self.size) #getting error when calling screen variable

    def move(self):
        self.x_coord = self.x_coord + self.x_dir
        self.y_coord = self.y_coord + self.y_dir
        #changing the direction of the ball object if it hits the edge of the screen
        if self.x_coord < 0 + self.size or self.x_coord > 640 - self.size:
            self.x_dir *= -1
        if self.y_coord < 0 + self.size or self.y_coord > 480 - self.size:
            self.y_dir *= -1

#list of balls - their x val, y val, and color
#ball_list = [[100, 100, WHITE], [200, 100, YELLOW], [300, 150, BLUE], [400, 180, BLUE]]
ball_color = [WHITE, BLUE, YELLOW]
balls = [] #balls will be a list of Ball() objects

for ball_data in range(150):
    #my_ball = Ball(random.randint(0,400), random.randint(0,400), BLUE)
    my_ball = Ball(random.randint(0, 640), random.randint(0,480), 1, 1, ball_color[random.randint(0, len(ball_color) - 1)])
    balls.append(my_ball) #add the new randomly generated 

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
     #Next event
    # -- Game logic goes after this comment
    # -- Screen background is BLACK
    screen.fill(BLACK)

    #select a ball from balls list - a list of ball objects
    for ball in balls:
        ball.draw(screen) #draw the ball
        ball.move() #move the ball

    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
