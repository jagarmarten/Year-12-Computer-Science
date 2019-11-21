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
pygame.font.init()

# -- Blank Screen
size = (640, 480)

screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")

#Classes & functions
class Invader(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed):
        #calling the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 50)
        self.speed = speed

    #update method
    def update(self):
        self.rect.y = self.rect.y + self.speed
    #End Procedure
#End Class

class Player(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, lives):
        #calling the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = size[1] - height
        self.speed = 0
        self.width = width
        self.height = height
        self.lives = lives

    #update method
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x > size[0] - self.width:
            self.rect.x = size[0] - self.width
            self.speed = 0
        if self.rect.x < 0:
            self.rect.x = 0
            self.speed = 0
    #End Procedure

    #set speed method
    def player_set_speed(self, value):
        self.speed = value
        print(self.rect.x)
    #end procedure
#End Class

# -- Exit game flag set to false
done = False

#list of all snow blocks
invader_group = pygame.sprite.Group()
#list of all sprites
all_sprites_group = pygame.sprite.Group()

player = Player(WHITE, 10, 10, 5)
all_sprites_group.add(player)

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#create x snowflakes
number_of_invaders = 10
for x in range(number_of_invaders):
    my_invader = Invader(BLUE, 10, 10, 1)
    invader_group.add(my_invader)
    all_sprites_group.add(my_invader)

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:  # - a key is down
            if event.key == pygame.K_LEFT:  # - if the left key pressed
                player.player_set_speed(-3)  # speed set to -3
            elif event.key == pygame.K_RIGHT:  # - if the right key pressed
                player.player_set_speed(3)  # speed set to 3
        elif event.type == pygame.KEYUP:  # - a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)  # speed set to 0
            #ENDIF
        #ENDIF
    #ENDFOR

    # -- Game logic goes after this comment
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    all_sprites_group.update() # update all sprites

    screen.fill(BLACK)  # -- Screen background is BLACK

    #font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 20, True, False)
    #create the text - text value, anti-aliasing, color
    text = font.render("Lives: " + str(player.lives), True, WHITE)
    # getting the size of the text rectangle - I'll use it later to center the text properly
    text_size = text.get_rect().width
    #put the text on the screen at a position in [ ]...
    screen.blit(text, [20, 20])

    all_sprites_group.draw(screen) # draw the list of all sprites to the screen

    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
