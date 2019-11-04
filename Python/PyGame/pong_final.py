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
+
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#ball and paddle sizes
ball_width = 20
paddle_width = 15
paddle_height = 60

#initial position of the ball
x_val = 250
y_val = 150

#direction of the ball on x & y axis
x_direction = 3
y_direction = 3

#initial position of the left paddle
x_pad_left = 0
y_pad_left = 0

#initial position of the right paddle
x_pad_right = size[0] - paddle_width
y_pad_right = 0

#user score
score_left = 0
score_right = 0

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
        y_pad_left = y_pad_left - 5
        if y_pad_left < 0:
            y_pad_left = 0
        #end if
    #end if
    if keys[pygame.K_DOWN]:
        y_pad_left = y_pad_left + 5
        if y_pad_left > size[1] - 60:
            y_pad_left = size[1] - 60
        #end if
    #end if
    if keys[pygame.K_s]:
        y_pad_right = y_pad_right + 5
        if y_pad_right > size[1] - 60:
            y_pad_right = size[1] - 60
        #end if
    #end if
    if keys[pygame.K_w]:
        y_pad_right = y_pad_right - 5
        if y_pad_right < 0:
            y_pad_right = 0
        #end if
    #end if

    # -- Next event
    # -- Game logic goes after this comment

    #changing the direction of the ball once it hits the left paddle
    if x_val < paddle_width and y_val > y_pad_left and y_val < y_pad_left + 60:
        x_direction = x_direction * -1
    #end if

    #changing the direction of the ball once it hits the right paddle
    if x_val >= size[0] - ball_width - paddle_width and y_val > y_pad_right and y_val < y_pad_right + 60:
        x_direction = x_direction * -1
    #end if

    #getting the current coordinates of the ball
    x_val = x_val + x_direction
    y_val = y_val + y_direction

    if y_val > (size[1] - ball_width) or y_val < (0):
        y_direction = y_direction * -1
    #end if
    #if x_val > (size[0] - ball_width) or x_val < (0):
    #    x_direction = x_direction * -1
    #end if

    if x_val  > size[0]:
        score_left = score_left + 1
        x_val = size[0]/2 - ball_width/2
        y_val = size[1]/2 - ball_width/2
    elif x_val < 0 - ball_width:
        score_right = score_right + 1
        x_val = size[0]/2 - ball_width/2
        y_val = size[1]/2 - ball_width/2
        pygame.time.delay(3000)

    #condition which prevents the paddles to go off the screen
    if (x_pad_left > 0 and y_pad_left > 0) or (x_pad_right > size[0] and y_pad_right > 0):
        y_pad_left = 0
        x_pad_left = 0
    #end if
    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width)) #drawing the ball
    pygame.draw.rect(screen, WHITE, (x_pad_left, y_pad_left, paddle_width, paddle_height)) #drawing the left paddle
    pygame.draw.rect(screen, WHITE, (x_pad_right, y_pad_right, paddle_width, paddle_height)) #drawing the right paddle

    #font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 40, True, False)
    #create the text - text value, anti-aliasing, color
    text = font.render(str(score_left) + " : " + str(score_right), True, WHITE)
    text_size = text.get_rect().width  # getting the size of the text rectangle - I'll use it later to center the text properly
    #put the text on the screen at a position in [ ]...
    screen.blit(text, [(size[0]/2) - (text_size/2), 0])

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- The clock ticks over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
