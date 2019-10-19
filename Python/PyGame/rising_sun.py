import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREEN = (128, 235, 52)
GRAY = (199, 199, 199)
DARK_GRAY = (99, 99, 99)
LIGHT_BLUE = (176, 247, 255)
RED = (235, 52, 52)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)

screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False

sun_x = 40
sun_y = 100

house_x = 220
house_y = 250
house_width = 200
house_height = 150

screen.fill(LIGHT_BLUE)
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
     #Next event
    # -- Game logic goes after this comment
    if sun_x == 640:
      sun_x=0
    else:
      sun_x = sun_x + 5

    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    pygame.draw.rect(screen, LIGHT_BLUE, (0,0,size[0],size[1]))
    pygame.draw.rect(screen, GRAY, (house_x,house_y,house_width,house_height))
    pygame.draw.rect(screen, DARK_GRAY, (house_x+20,house_y+30,80,60))
    pygame.draw.rect(screen, DARK_GRAY, ((house_x+house_height-30),house_y+30,60,(house_height-30)))
    pygame.draw.rect(screen, GREEN, (0,house_y + 150,640,80))
    pygame.draw.polygon(screen, RED, [[320, 170], [200, 250], [440, 250]])
    
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), 40, 0)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
     # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

