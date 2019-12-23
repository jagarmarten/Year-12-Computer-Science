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
    def __init__(self, color, width, height, speed, invader_image):
        #calling the sprite constructor
        super().__init__()

        self.image = pygame.image.load("small.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 50)
        self.speed = speed

    #update method
    def update(self):
        self.rect.y = self.rect.y + self.speed
        self.image = pygame.image.load("small.png")
    #End Procedure
#End Class

class Bullet(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed, x_coordinate):
        #calling the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x_coordinate + 22.5 #22.5 because I wanted to center the bullet to fire from the cannon
        self.rect.y = size[1] - height - 26

    #update method
    def update(self):
        self.rect.y = self.rect.y - self.speed
    #End Procedure
#End Class

class Player(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, width, height, lives, bullet_count):
        #calling the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.image.load("cannon.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = size[1] - height
        self.speed = 0
        self.width = width
        self.height = height
        self.lives = lives
        self.bullet_count = bullet_count

    #update method
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x > size[0] - self.width:
            self.rect.x = size[0] - self.width
            self.speed = 0
        if self.rect.x < 0:
            self.rect.x = 0
            self.speed = 0
        self.image = pygame.image.load("cannon.png")
    #End Procedure

    #set speed method
    def player_set_speed(self, value):
        self.speed = value
    #end procedure
#End Class

# -- Exit game flag set to false
done = False

#list of all snow blocks
invader_group = pygame.sprite.Group()
#list of all sprites
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player(46, 28, 5, 50)
all_sprites_group.add(player)

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#adding a background image
background_image = pygame.image.load("invaders.png").convert()

#create x snowflakes
number_of_invaders = 10
for x in range(number_of_invaders):
    my_invader = Invader(BLUE, 10, 10, 1, "cannon.png")
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
            elif event.key == pygame.K_SPACE:
                #creating bullets when space bar is pressed
                if player.bullet_count == 0:
                    pass
                else:
                    bullet = Bullet(YELLOW, 2, 10, 2, player.rect.x)
                    bullet_group.add(bullet)
                    player.bullet_count -= 1
                    all_sprites_group.add(bullet) 
        elif event.type == pygame.KEYUP:  # - a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)  # speed set to 0
            #ENDIF
        #ENDIF
    #ENDFOR

    #ALex helped me with this one
    for bullet_shot in bullet_group:
        invader_hit_group = pygame.sprite.spritecollide(bullet_shot, invader_group, True)
        for bullet_shot in invader_hit_group:
                bullet_group.remove(bullet)
                all_sprites_group.remove(bullet)
        if bullet.rect.y < 0:
                bullet_group.remove(bullet)
                all_sprites_group.remove(bullet)

    # -- Game logic goes after this comment
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    # update all sprites
    all_sprites_group.update()

    #loading the background image
    screen.blit(background_image, [-60, 0])

    #font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 20, True, False)
    #create the text - text value, anti-aliasing, color
    lives = font.render("Lives: " + str(player.lives), True, WHITE)
    bullets_left = font.render("Bullets: " + str(player.bullet_count), True, WHITE)
    # getting the size of the text rectangle - I'll use it later to center the text properly
    text_size = lives.get_rect().width
    text_size2 = bullets_left.get_rect().width
    #put the text on the screen at a position in [ ]...
    screen.blit(lives, [20, 20])
    screen.blit(bullets_left, [20, 45])

    all_sprites_group.draw(screen) # draw the list of all sprites to the screen

    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
