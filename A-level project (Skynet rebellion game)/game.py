# -- Import and initialize the pygame library
import pygame # - Import pygame library
import math # - Import math library
import random # - Import random library
from pygame.locals import * # - Pygame.locals gives us the access to key coordinates, ...
pygame.init() # - Initialize the pygame library

from classes import *


# Set up the drawing window
screen = pygame.display.set_mode([800, 600]) # - Set up a new scree of the size 800 x 600 pixels

# VARIABLES & CONSTANTS
# - Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)

# - Create an instance of the Player class
player = Player(50, 50, 100, 50, BLACK, 1)
# - Create a player group
player_group = pygame.sprite.Group()
player_group.add(player) #add player to the player_group
# - Create a platform group
platform_group = pygame.sprite.Group()
# - Create an all_sprites group
all_sprites_group = pygame.sprite.Group()
# - Add the player_group and platform_group to the all_sprites_group
all_sprites_group.add(player_group)
all_sprites_group.add(platform_group)

# - Run until the user asks to Quit
running = True

# -- Main while loop
while running:
    # -- Close the window if the user clicks the Quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # - Fill the background with white
    screen.fill((255, 255, 255))

    all_sprites_group.draw(screen)
    
    # -- Draw here:

    # -- Flip the display
    pygame.display.flip()

# -- Exit the pygame
pygame.quit()
