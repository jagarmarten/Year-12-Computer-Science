# - GAME.PY
import pygame  # -- import the pygame library
from pygame.locals import * # -- pygame.locals is a module that contains various pygame constants
pygame.init()  # -- initialize the pygame library
pygame.font.init() # -- initialize the font module

pygame.display.set_caption('Skynet Rebellion') # -- set the name of the window to 'Skynet Rebellion'
screen = pygame.display.set_mode([800, 600]) # -- create a screen with a resolution of 800 by 600

FPS = 60 # -- frames per second
fpsClock = pygame.time.Clock() # -- initialize the pygame.time.Clock() object

fontOne = pygame.font.Font('teko.ttf', 90) # -- import the font Teko from the system and set it to size 70
fontTwo = pygame.font.Font('teko.ttf', 30) # -- import the font Teko from the system and set it to size 25

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
    [300, 30, 400, 550],
    [300, 30, 650, 500],
    [300, 30, 400, 400],
    [300, 30, 820, 300],
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

# - DRAW TEXT FUNCTION
# -- parameters: text, font, colour, surface, x-coord and y-coord, coordinates_method
def draw_text(text, font, colour, surface, x_coord, y_coord, coordinates_method):
    textToDisplay = font.render(text, False, colour) # -- render a text with a colour
    textToDisplayRectObj = textToDisplay.get_rect() # -- get the rect object of the text

    # -- check for the coordinates method
    if coordinates_method == "center":
        textToDisplayRectObj.center = (x_coord, y_coord) # -- set the center values to x-coord and y-coord
    elif coordinates_method == "top-right":
        textToDisplayRectObj.topright = (x_coord, y_coord) # -- set the top right values to x-coord and y-coord
    elif coordinates_method == "top-left":
        textToDisplayRectObj.topleft = (x_coord, y_coord) # -- set the center values to x-coord and y-coord
    # - END IF

    surface.blit(textToDisplay, textToDisplayRectObj) # -- display the text on the screen
# - END FUNCTION

# - MOUSE POSITION FUNCTION
def mouse_position():
    return pygame.mouse.get_pos() # -- return the position of the mouse
# - END FUNCTION

click = False
# - MAIN MENU FUNCTION
def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 255)) # -- fill the screen with blue colour
        
        draw_text('SKYNET REBELLION', fontOne, (0,0,0), screen, 400, 270, "center") # -- render a "SKYNET REBELLION" text on the screen with a black colour, and coordinates x=100 y=300

        mouse_x, mouse_y = mouse_position() # -- get the mouse_x and mouse_y

        mainMenuPlayButton = pygame.Rect(0, 0, 400, 50) # -- create a new rect object with coordinates x=0, y=0 and witdh=400, height=50
        mainMenuPlayButton.center = (400, 370) # -- set the center coordinates to x=400, y=370

        # -- if the mouse_x and mouse_y collides with the mainMenuPlayButton
        if mainMenuPlayButton.collidepoint((mouse_x, mouse_y)):
            # -- if the user clicks on the button
            if click:
                game() # -- run the game function
        # - END IF

        pygame.draw.rect(screen, (255, 0, 0), mainMenuPlayButton) # -- draw the rect object on the screen
        draw_text('START GAME', fontTwo, (0,0,0), screen, 400, 370, "center") # -- render a "SKYNET REBELLION" text on the screen with a black colour, and coordinates x=100 y=300

        click = False # -- set click to False

        pygame.display.update() # -- update the display
        # - FOR loop which listens to events
        for event in pygame.event.get():
            # -- if user quits the game
            if event.type == pygame.QUIT:
                running = False # -- set running to false
                pygame.quit() # -- quit pygame
            # - END IF

            # -- if a key is pressed
            if event.type == pygame.KEYDOWN:
                # -- if an escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    running = False # -- set running to false
                    pygame.quit() # -- quit pygame
            # - END IF

            # -- if he user clicks with the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # -- if it's a left click
                if event.button == 1:
                    click = True # -- set the variable click to true
            # - END IF
        # - END FOR
    pygame.quit() # -- quit the game
# - END FUNCTION

# - PAUSE FUNCTION
def pause():
    paused = True # -- set paused to True
    # -- while paused is set to True:
    while paused:
        screen.fill((255, 255, 255)) # -- fill the screen with black colour
        mouse_x, mouse_y = mouse_position() # -- get the mouse_x and mouse_y

        unpauseButton = pygame.Rect(0, 0, 400, 50) # -- create a new rect object with coordinates x=0, y=0 and witdh=400, height=50
        unpauseButton.center = (400, 370) # -- set the center coordinates to x=400, y=370

        # -- if the mouse_x and mouse_y collides with the unpauseButton
        if unpauseButton.collidepoint((mouse_x, mouse_y)):
            # -- if the user clicks on the button
            if click:
                paused = False # -- set paused to False
            # - END IF
        # - END IF

        pygame.draw.rect(screen, (255, 0, 0), unpauseButton) # -- draw the rect object on the screen
        draw_text('RESUME GAME', fontTwo, (0,0,0), screen, 400, 370, "center") # -- render a "RESUME GAME" text on the screen with a black colour, and coordinates x=400 y=370

        click = False # -- set click to False
        pygame.display.update() # -- update the display
        for event in pygame.event.get():
            # -- if user quits the game
            if event.type == pygame.QUIT:
                pygame.quit() # -- quit the game
                quit() # -- quit the program
            # - END IF

            # -- if a key is pressed
            if event.type == pygame.KEYDOWN:
                # -- if an escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() # -- quit the game
                    quit() # -- quit the program
                # - END IF

                # -- if an c key is pressed
                if event.key == pygame.K_c:
                    paused = False # -- set paused to False
                # - END IF
            # - END IF

            # -- if he user clicks with the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # -- if it's a left click
                if event.button == 1:
                    click = True # -- set the variable click to true
                # -- END IF
            # - END IF
        # - END FOR

        draw_text('GAME PAUSED', fontOne, (0,0,0), screen, 400, 270, "center") # -- render a "GAME PAUSED" text on the screen

        pygame.display.update() # -- update the display
        fpsClock.tick(5) # -- set the display to 5fps
    # - END WHILE
# - END FUNCTION

# - GAME FUNCTION
def game():
    running = True # -- variable running set to true
    click = False # -- set click to False
    lives = 3 # -- set lives to 3
    score = 0 # -- set score to 0
    # - game() while loop
    while running:
        screen.fill((0, 0, 0)) # -- fill the screen with black colour
        mouse_x, mouse_y = mouse_position() # -- get the mouse_x and mouse_y

        pauseButton = pygame.Rect(0, 0, 40, 40) # -- create a new rect object with coordinates x=0, y=0 and witdh=400, height=50
        pauseButton.topright = (790, 10) # -- set the center coordinates to x=400, y=370

        # -- if the mouse_x and mouse_y collides with the pauseButton
        if pauseButton.collidepoint((mouse_x, mouse_y)):
            # -- if the user clicks on the button
            if click:
                pause() # -- run the pause() function
            # - END IF
        # - END IF

        pygame.draw.rect(screen, (255, 0, 0), pauseButton) # -- draw the rect object on the screen
        draw_text('| |', fontTwo, (255,255,255), screen, 780, 10, "top-right") # -- render a "| |" text on the screen

        draw_text("Lives left: " + str(lives), fontTwo, (255,255,255), screen, 20, 10, "top-left") # -- render "Lives left: " text on the screen
        draw_text("Score: " + str(score), fontTwo, (255,255,255), screen, 140, 10, "top-left") # -- render "Score" text on the screen

        click = False # -- set click to False
        # - FOR loop which listens to events
        for event in pygame.event.get():
            # -- if user quits the game
            if event.type == pygame.QUIT:
                running = False # -- set the variable running to False
            # - END IF

            # -- if a key is pressed
            if event.type == pygame.KEYDOWN:
                # -- if an escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    running = False # -- set running to false
                # - END IF
            # - END IF

            # -- if he user clicks with the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # -- if it's a left click
                if event.button == 1:
                    click = True # -- set the variable click to true
                # - END IF
            # - END IF
        # - END FOR

        all_sprites_group.draw(screen) # -- Draw all the sprites on the screen
        all_sprites_group.update() # -- Run the Update method on all_sprites_group

        # -- If the player and platforms_group collide,
        if collision(player, platforms_group) == True:
            player.player_on_platform = True # -- Set the player_on_platform to True
            player.rect.bottom = collisionCoordinates(player, platforms_group)[0].rect.top # -- set the bottom y-value of player to the top y-value of the platform
        else:
            player.player_on_platform = False # -- Set the player_on_platform to False
        # -- END IF

        pygame.display.update() # -- update the display
        fpsClock.tick(FPS) # -- set the display to 60fps
    # - END WHILE
    pygame.quit() # -- quit the game
# - END FUNCTION

main_menu() # -- calling the main_menu function, so that it's the first executed