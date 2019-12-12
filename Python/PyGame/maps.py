import random
import math
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
pygame.display.set_caption("Maps")

# -- flip display to reveal new position of objects
# Create an address
# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### Classes, functions, arrays and custom variables
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

## -- Define the class tile which is a sprite
class Tile(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        
class Player(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.x_speed = 0
        self.y_speed = 0

    def player_update_speed(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed

# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()
# Create a list of tiles for the walls
wall_list = pygame.sprite.Group()

# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range (10):
        if map[x][y] == 1:
            my_wall = Tile(BLUE, 20, 20, x*20, y *20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)
        #end if
    #end for
#end for
pacman = Player(YELLOW, 10, 10, 20, 20)

all_sprites_list.add(pacman)

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #endif
    #next event
    
    
    #key press handlers
    if event.type == pygame.KEYDOWN:  # - a key is pressed down
        if event.key == pygame.K_LEFT:  # - if the left key pressed
            pacman.player_update_speed(-2, 0)
        elif event.key == pygame.K_RIGHT:  # - if the right key pressed
            pacman.player_update_speed(2, 0)
        elif event.key == pygame.K_UP:  # - if the left key pressed
            pacman.player_update_speed(0, -2)
        elif event.key == pygame.K_DOWN:  # - if the right key pressed
            pacman.player_update_speed(0, 2)
        #endif
    #endif

    # -- Check for collisions between pacman and wall tiles
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_list, False)
    for foo in player_hit_list:
        pacman.player_update_speed(0, 0)
        pacman.rect.x = pacman_old_x
        pacman.rect.y = pacman_old_y
    # Run the update function for all sprites
    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y
    all_sprites_list.update()
    

    # -- Screen background is BLACK
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    # -- Game logic goes after this comment
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
