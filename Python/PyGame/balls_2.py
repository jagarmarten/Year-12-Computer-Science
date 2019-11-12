import pygame
# -- Global Constants

# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)

# -- Initialise PyGame
pygame.init()

# -- flip display to reveal new position of objects
# Create an address
# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#Classes & functions
class Screen():
    def __init__(self, x_val, y_val, caption):
        self.x = x_val
        self.y = y_val
        self.caption = caption
        pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption(self.caption)

    ## fill doesn't work yet
    def fill(self, fill_color):
        self.color = fill_color
    
class Ball():
    def __init__(self, x, y, col):
        self.color = col
        self.x_coord = x
        self.y_coord = y
        self.size = 10

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_coord, self.y_coord), self.size) #getting error when calling screen variable

    def move(self):
        self.x_coord += 2
        self.y_coord += 2

    #def balls(self, list_of_balls):
        #self.list_of_balls = list_of_balls
        #for ball in list_of_balls:
            #ball = Ball(ball[0], ball[1], ball[2])
            #ball.draw()
            #ball.move()

balls_list = [[100, 100, WHITE], [200, 100, YELLOW], [300, 150, BLUE]]

one = Ball(balls_list[0][0], balls_list[0][1], balls_list[0][2])
two = Ball(balls_list[1][0], balls_list[1][1], balls_list[1][2])

screen = Screen(640, 480, "Snow")

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

    #####
    #I'm unable to move those balls around the screen
    #####
    for ball in balls_list:
        ball = Ball(ball[0], ball[1], ball[2])
        ball.draw(screen)
        ball.move()

    one.draw(screen)
    one.move()

    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
