# -- Import and initialize the pygame library
import pygame # - Import pygame library
from pygame.locals import * # - Pygame.locals gives us the access to key coordinates, ...
pygame.init() # - Initialize the pygame library

# Set up the drawing window
screen = pygame.display.set_mode([800, 600]) # - Set up a new scree of the size 800 x 600 pixels

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

    # -- Draw here:

    # -- Flip the display
    pygame.display.flip()

# -- Exit the pygame
pygame.quit()
