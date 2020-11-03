# This file contains all the constants used in the game
# - SCREEN CONSTANTS
WIDTH = 800
HEIGHT = 600


# - COLORS
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 128)
LIGHTBLUE = (0, 0, 255)
RED = (200, 0, 0)
LIGHTRED = (255, 100, 100)
PURPLE = (102, 0, 102)
LIGHTPURPLE = (153, 0, 153)
BLACK = (0, 0, 0)
SHADOW = (192, 192, 192)

# - OTHER CONSTANTS
GRAVITY = 1

# - PLATFORMS - it's an array used for quicker creation of platforms and levels
PLATFORMS_MAP = [(0, HEIGHT - 20, WIDTH, 20, GREEN),
                 (200, HEIGHT - 80, 300, 20, RED),
                 (450, HEIGHT- 150, 150, 20, BLUE),
                 (600, HEIGHT - 200, 100, 20, LIGHTBLUE)]