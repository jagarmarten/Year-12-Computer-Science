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
pygame.display.set_caption("Snow")

#Classes & functions
class Snow(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height):
        #calling the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
    #End Procedure
#End Class

# -- Exit game flag set to false
done = False

#list of all snow blocks
snow_group = pygame.sprite.Group()
#list of all sprites
all_sprites_group = pygame.sprite.Group()

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()


#create x snowflakes
for x in range(50):
    my_snow = Snow(WHITE, 3, 3)
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)

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

    #draw the list of all sprites to the screen
    all_sprites_group.draw(screen) 

    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
