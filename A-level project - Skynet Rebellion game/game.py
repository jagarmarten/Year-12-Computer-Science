# - GAME.PY
import pygame  # -- import the pygame library
from pygame.locals import * # -- pygame.locals is a module that contains various pygame constants
pygame.init()  # -- initialize the pygame library

pygame.display.set_caption('Skynet Rebellion') # -- set the name of the window to 'Skynet Rebellion'
screen = pygame.display.set_mode([800, 600]) # -- create a screen with a resolution of 800 by 600

running = True # -- variable 'running' is used to stop the game if the user closes the window

# - PLAYER CLASS
# -- attributes: 
class Player(pygame.sprite.Sprite):
    # - Constructor method
    def __init__(self):
        super().__init__() # -- calling the methods of the superclass
        self.image = pygame.Surface([50, 100]) # -- create a new surface - 50 by 100px
        self.image.fill((255,255,255)) # -- fill the surface with white colour
        self.rect = self.image.get_rect() # -- catch the object which has the dimension of the image
        self.rect.x = 250 # -- set the x coordinate
        self.rect.y = 100 # -- set the y coordinate
        self.player_on_platform = True # -- player standing on the platform
    # - END Constructor method

    # - Update method
    def update(self):
        key_pressed = pygame.key.get_pressed() # -- check if a key was pressed
        
        # -- if the left arrow key was pressed,
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 3 # -- move the sprite 3 pixels to the left
        
        # -- if the right arrow key was pressed,
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += 3 # -- move the sprite 3 pixels to the right

        # -- if the spacebar was pressed,
        if key_pressed[pygame.K_SPACE]:
            self.jump() # -- call the jump() method

        self.gravity() # -- call the gravity() method
    # - END Update method

    # - Gravity method
    def gravity(self):
        # -- if player_on_platform is set to False,
        if self.player_on_platform == False:
            self.rect.y = self.rect.y + 3 # -- add 3 pixels to the y-direction
    # - END Gravity method

    # - Jump method
    def jump(self):
        # -- check whether the player is on the platform,
        if self.player_on_platform == True:
            self.rect.y -= 100 # -- move the player sprite 100 pixels upwards
    # - END Jump method
# - END CLASS

# - Platform CLASS
# -- attributes: width, height, x_coord, y_coord
class Platform(pygame.sprite.Sprite):
    # - Constructor method
    def __init__(self, width, height, x_coord, y_coord):
        super().__init__() # -- calling the methods of the superclass
        self.image = pygame.Surface([width, height]) # -- create a new surface - width by height pixels (depends on the parameters passed)
        self.image.fill((0,128,0)) # -- fill the surface with white colour
        self.rect = self.image.get_rect() # -- catch the object which has the dimension of the image
        self.rect.x = x_coord # -- set the x coordinate
        self.rect.y = y_coord # -- set the y coordinate
    # - END Constructor method

    # - Update method
    def update(self):
        key_pressed = pygame.key.get_pressed() # -- check if a key was pressed
        
        # -- if the left arrow key was pressed,
        if key_pressed[pygame.K_LEFT]:
            self.rect.x += 3 # -- move the sprite 3 pixels to the left
        
        # -- if the right arrow key was pressed,
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x -= 3 # -- move the sprite 3 pixels to the right
    # - END Update method
# - END CLASS

# - collision FUNCTION
def collision(group_one, group_two):
    hit = pygame.sprite.spritecollide(group_one, group_two, False) # -- check whether group_one and group_two collided
    # -- the two groups collide, do this:
    if hit:
        print("hit") # -- print "hit" in the console
        return True # -- return True
    else:
        return False # -- return False if the two groups are not colliding
# - END FUNCTION

# - collisionCoordinates FUNCTION
def collisionCoordinates(group_one, group_two):
    return pygame.sprite.spritecollide(group_one, group_two, False) # -- return the spritecollide object
# - END FUNCTION

# - platforms array
# -- width, height, x and y-coordinates of the platform
platforms = [
    [300, 30, 200, 350],
    [300, 30, 100, 250],
    [300, 30, 400, 550]
]
# - END platforms array

player = Player() # -- create an instance of the Player class

platforms_group = pygame.sprite.Group() # -- create a platforms group

# - platforms for loop
# -- this for loop is responsible for creating platform instances from an array
for platform in platforms:
    platform_sprite = Platform(platform[0], platform[1], platform[2], platform[3]) # -- create an instance of a Platform, and pass in the parameters from the platforms array
    platforms_group.add(platform_sprite) # -- add the instance of Platform class (platform_sprite) to the platform_group
# - END platforms for loop

all_sprites_group = pygame.sprite.Group() # -- create a new sprite group
all_sprites_group.add(player) # -- add the player sprite into all_sprites_group
all_sprites_group.add(platforms_group) # -- add the platform_group into all_sprites_group

# - MAIN WHILE LOOP
# -- this is where the game is being executed
while running:
    
    # - FOR loop which listens to events
    for event in pygame.event.get():
        # -- if user quits the game
        if event.type == pygame.QUIT:
            running = False # -- set the variable running to False
        # - END IF
    # - END FOR

    screen.fill((0, 0, 0)) # -- fill the screen with white colour

    all_sprites_group.draw(screen) # -- Draw all the sprites on the screen
    all_sprites_group.update() # -- Run the Update method on all_sprites_group

    # -- If the player and platforms_group collide,
    if collision(player, platforms_group) == True:
        player.player_on_platform = True # -- Set the player_on_platform to True
        player.rect.bottom = collisionCoordinates(player, platforms_group)[0].rect.top # -- set the bottom y-value of player to the top y-value of the platform
    else:
        player.player_on_platform = False # -- Set the player_on_platform to False
    # -- END IF

    pygame.display.flip() # -- Flip the display
    pygame.time.Clock().tick(60) # -- set the number of frames per second to 60
# - END WHILE

pygame.quit() # - Exit the game