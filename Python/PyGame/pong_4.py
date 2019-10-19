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
pygame.display.set_caption("Pong")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

ball_width = 20
paddle_width = 15
paddle_height = 60

x_val = 250
y_val = 150

x_pad = 0
y_pad = 0

x_direction = -1
y_direction = 0

# -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # End If
    # End for

    ## - the up key or down key has been pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_pad = y_pad - 5
        if y_pad < 0:
            y_pad = 0
        #end if
    #end if
    if keys[pygame.K_DOWN]:
        y_pad = y_pad + 5
        if y_pad > size[1] - 60:
            y_pad = size[1] - 60
        #end if
    #end if

    # -- Next event
    # -- Game logic goes after this comment
    x_val = x_val + x_direction
    y_val = y_val + y_direction

    if y_val > (size[1] - ball_width) or y_val < (0):
        y_direction = y_direction * -1
    #end if
    if x_val > (size[0] - ball_width) or x_val < (0):
        x_direction = x_direction * -1
    #end if
    #changing the direction of the ball once it hits the paddle
    #if x_val <= 15 and y_val >= y_pad and y_val <= y_pad + 60:
    #    y_direction = y_direction * -1
    if x_val <= 15 and y_val >= y_pad and y_val <= y_pad + 60:
        x_direction = x_direction * -1
    #if x_val >= 0 and x_val <= 15
    #end if
    if x_pad > 0 and y_pad > 0:
        y_pad = 0
        x_pad = 0
    #end if
    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
    pygame.draw.rect(screen, WHITE, (x_pad, y_pad, paddle_width, paddle_height))
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- The clock ticks over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
