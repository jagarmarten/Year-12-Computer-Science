# -- Import and initialize the pygame library
import pygame  # - Import pygame library
import math  # - Import math library
import random  # - Import random library
from pygame.locals import * # - Pygame.locals gives us the access to key coordinates, ...

# - PLAYER CLASS
# -- properties: x-pos, y-pos, width, height, color & speed
class Player(pygame.sprite.Sprite):
    # Define the constructor for player
    def __init__(self, x_pos, y_pos, width, height, color, speed):
        # -- Calling the sprite constructor
        super().__init__()
        self.image = pygame.Surface([width, height])  # -- Create a sprite
        self.image.fill(color)  # -- Fill the sprite with a color
        # -- Get the rectangular values for easier positioning
        self.rect = self.image.get_rect()
        self.rect.x = x_pos  # -- Set the x_position
        self.rect.y = y_pos  # -- Set the y_position
        self.speed = speed  # -- Set the speed
        self.color = color  # -- Set the color

    # - UPDATE Method
    def update(self):
        # -- Every key pressed will get stored into the keys variable
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
    #End Procedure
# - END OF PLAYER CLASS

# - PLATFORM CLASS
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()  # -- Calling the sprite constructor
        self.image = pygame.Surface([width, height])  # -- Create a sprite
        self.image.fill(color)  # -- Fill the sprite with a color
        # -- Get the rectangular values for easier positioning
        self.rect = self.image.get_rect()
        self.rect.x = x  # -- Set the x_position
        self.rect.y = y  # -- Set the y_position
        self.color = color  # -- Set the color
# - END OF PLATFORM CLASS
