import pygame
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

    def __init__(self, x, y, col):
        self.color = col
        self.x_coord = x
        self.y_coord = y
        self.size = 10

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x_coord, self.y_coord), self.size)

    def move(self):
        self.x_coord += 2
        self.y_coord += 2


one = Ball(100, 100, WHITE)
two = Ball(200, 200, YELLOW)

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

    one.draw()
    one.move()

    two.draw()
    two.move()

    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
