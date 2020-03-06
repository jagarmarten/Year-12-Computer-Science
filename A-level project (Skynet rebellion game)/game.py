# -- Import and initialize the pygame library
import pygame # - Import pygame library
import math # - Import math library
import random # - Import random library
from pygame.locals import * # - Pygame.locals gives us the access to key coordinates, ...
pygame.init() # - Initialize the pygame library

from classes import * # - Import everything from classes.py
from constants import * # - Import everything from constants.py

# Set up the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # - Set up a new scree of the size 800 x 600 pixels

# - Create an instance of the Player class
player = Player(0, 0, 20, 35, BLACK, 1)
player_group = pygame.sprite.Group()  # -- Create a player_group
player_group.add(player) #add player to the player_group

# - Create a platform group
platform = Platform(0, HEIGHT - 20, WIDTH, 20, GREEN) # - Create a full-width platform located at the bottom 
platform_group = pygame.sprite.Group() # -- Create a platform_group
platform_group.add(platform) # -- Add the platform to the platform_group

# - Create an all_sprites group
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player_group) # -- Add the player_group to all_sprites_group
all_sprites_group.add(platform_group) # -- Add the platform_group to all_sprites_group

# - Run until the user asks to Quit
running = True

# - MAIN WHILE LOOP
while running:
    # - Event listener
    for event in pygame.event.get():
        # -- CLose the window if the user clicks the close button
        if event.type == pygame.QUIT:
            running = False

    # - Fill the background with white
    screen.fill((255, 255, 255))

    # -- Draw here:
    all_sprites_group.draw(screen) # -- Draw all the sprites on the screen
    all_sprites_group.update() # -- Update all the sprites

    # -- Check whether the player has collided with the platform
    hit = pygame.sprite.spritecollide(player, platform_group, False) # -- False means don't delete it
    # -- If the sprites collide, do this:
    if hit:
        player.pos[1] = hit[0].rect.top # -- Set the player Y position to hit[0].rect.top
        player.gravity = 0 # -- Preventing the player from further falling down
        #print(hit[0].rect.top)
        #print(player.pos[1])

    # -- Flip the display
    pygame.display.flip()

# -- Exit the pygame
pygame.quit()
# - END OF THE MAIN WHILE LOOP
