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

x_val = 150
y_val = 200

x_pad = 0
y_pad = 0

x_direction = 1
y_direction = 1

# -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # End If
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_pad = y_pad - 20
            elif event.key == pygame.K_DOWN:
                y_pad = y_pad + 20
            #End If
        #endif
    # -- Next event
    # -- Game logic goes after this comment
    x_val = x_val + x_direction
    y_val = y_val + y_direction

    if y_val > (size[1] - ball_width) or y_val < (0):
        y_direction = y_direction * -1

    if x_val > (size[0] - ball_width) or x_val < (0):
        x_direction = x_direction * -1
    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
    pygame.draw.rect(screen, WHITE, (x_pad, y_pad, 15, 60))
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- The clock ticks over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
