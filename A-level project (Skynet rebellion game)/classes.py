# -- Import and initialize the pygame library
import pygame  # - Import pygame library
import math  # - Import math library
import random  # - Import random library
from pygame.locals import * # - Pygame.locals gives us the access to key coordinates, ...

from constants import *  # - Import everything from constants.py

# - PLAYER CLASS
# -- properties: x-pos, y-pos, width, height, color & speed
class Player(pygame.sprite.Sprite):
    # - CONSTRUCTOR
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
        self.pos = [0, 0] # -- Default position of the player
        self.gravity = 1 # -- Speed by which the user will fall down
        self.isJumping = False # -- Variable used later in the jump() method
        self.isOnPlatform = False # -- Variable used to prevent the player from jumping multiple times when pressing space
        self.maxJump = 200 # -- Maximum jump height
    # - END CONSTRUCTOR

    # - UPDATE Method
    def update(self):
        # -- Every key pressed will get stored into the keys variable
        keys = pygame.key.get_pressed()
        # -- If the left key is pressed, do this:
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1 # -- Move the sprite 1 to the left
        # -- If the right key is pressed, do this:
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1 # -- Move the sprite 1 to the right

        self.rect.y += self.gravity # -- Make the user fall by default

        # -- self.rect.midbottom gives us the middle X value and bottom Y value of the sprite
        self.pos[0] = self.rect.midbottom[0] # -- set the self.pos[0] to the midbottom X value
        self.pos[1] = self.rect.midbottom[1] # -- set the self.pos[1] to the midbottom Y value
    # - END METHOD

    # - JUMP METHOD
    def jump(self):
        # -- If the player.isJumping is set to True, do this:
        if self.isJumping:
            # -- If the maxJump is greater than 0, do this:
            if self.maxJump >= 0:
                self.maxJump -= 1 # -- Make the maxJump lower by 1 with each iteration
                self.rect.y -= 2 # -- Jump by 2 steps in the Y direction
            else:
                self.isJumping = False # -- Once the jumping is done, set the isJumping back to False
                self.maxJump = 200 # -- set the maxJump to the default value
            # - END JUMP IF
        # - END IF
    # - END METHOD
# - END OF PLAYER CLASS

# - PLATFORM CLASS
class Platform(pygame.sprite.Sprite):
    # - CONSTRUCTOR
    def __init__(self, x, y, width, height, color):
        super().__init__()  # -- Calling the sprite constructor
        self.image = pygame.Surface([width, height])  # -- Create a sprite
        self.image.fill(color)  # -- Fill the sprite with a color
        # -- Get the rectangular values for easier positioning
        self.rect = self.image.get_rect()
        self.rect.x = x  # -- Set the x_position
        self.rect.y = y  # -- Set the y_position
        self.color = color  # -- Set the color
    # - END CONSTRUCTOR
# - END OF PLATFORM CLASS
