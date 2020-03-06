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
player = Player(20, 20, 20, 35, BLACK, 1)
player_group = pygame.sprite.Group()  # -- Create a player_group
player_group.add(player) #add player to the player_group

# - Create a platform group
p1 = Platform(0, HEIGHT - 20, WIDTH, 20, GREEN) # - Create a full-width platform located at the bottom 
p2 = Platform(20, HEIGHT - 100, 100, 20, LIGHTGREEN)
p3 = Platform(WIDTH - 600, HEIGHT - 150, 200, 20, BLUE)
p4 = Platform(WIDTH - 500, HEIGHT - 500, 200, 40, PURPLE)
platform_group = pygame.sprite.Group() # -- Create a platform_group
platform_group.add(p1) # -- Add the platform to the platform_group
platform_group.add(p2)  # -- Add the platform to the platform_group
platform_group.add(p3)  # -- Add the platform to the platform_group
platform_group.add(p4)  # -- Add the platform to the platform_group

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.isOnPlatform == True:
                    player.isJumping = True # -- isJumping is a property of the Player object which is False by default
                    player.isOnPlatform = False # -- bolean used to check whether the player is on the platform (using the hit group)

    # - Fill the background with white
    screen.fill((255, 255, 255))

    # -- Draw here
    all_sprites_group.draw(screen) # -- Draw all the sprites on the screen
    all_sprites_group.update() # -- Update all the sprites
    player.jump() # -- Player will jump if isJumping is True

    # -- Check whether the player has collided with the platform
    hit = pygame.sprite.spritecollide(player, platform_group, False) # -- False means don't delete it
    # -- If the sprites collide, do this:
    if hit:
        player.pos[1] = hit[0].rect.top # -- Set the player Y position to hit[0].rect.top
        player.gravity = 0 # -- Preventing the player from further falling down
        player.isOnPlatform = True # -- Setting the isOnPlatform to true since the player sprite is on the platform
    else:
        player.gravity = 1 # -- Set the gravity to 1 if the player goes off a platform

    # -- Flip the display
    pygame.display.flip()

# -- Exit the pygame
pygame.quit()
# - END OF THE MAIN WHILE LOOP
