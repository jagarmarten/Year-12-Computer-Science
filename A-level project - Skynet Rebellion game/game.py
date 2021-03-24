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
        self.rect.y = 0 # -- set the y coordinate
        self.player_on_platform = True # -- player standing on the platform

        self.change_x = 0 # -- setting the speed vector of the player (x direction)
        self.change_y = 0 # -- setting the speed vector of the player (y direction)

        self.level = None # -- setting the level to none
    # - END Constructor method

    # - Update method
    def update(self):
        self.gravity() # -- calculate the gravity
        self.rect.x += self.change_x # -- move the player sprite to the left or right

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_group, False) # -- see if we hit a platform
        # -- loop through the block_hit_list
        for block in block_hit_list:
            # -- if the player sprite is moving to the right and hits an object
            if self.change_x > 0:
                self.rect.right = block.rect.left # -- set our right side to the left side of the item hit
            elif self.change_x < 0:
                self.rect.left = block.rect.right # -- set the left side to the right side of the item hit
            # -- END IF
        # -- END FOR

        self.rect.y += self.change_y # -- move the player sprite up and down
 
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_group, False) # -- see if we hit a platform
        # -- loop through the block_hit_list
        for block in block_hit_list:
            # -- if the player sprite is moving downwards and hits an object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top # -- set our bottom side to the top side of the item hit
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom # -- set our top side to the bottom side of the item hit
            # -- END IF
            self.change_y = 0 # -- stop the vertical movement
        # -- END for
    # - END Update method
 
    # - Gravity method
    def gravity(self):
        # -- if the change_y value is 0:
        if self.change_y == 0:
            self.change_y = 1 # -- set change_y to 1
        else:
            self.change_y += 0.35 # -- otherwise add 0.35 to change_y
        # -- END IF
    # - END Gravity method

    # - Move_left method
    def move_left(self):
        self.change_x = -3
    # - END Move_left method
 
    # - Move_right method
    def move_right(self):
        self.change_x = 3
    # - Move_right method

    # - stop method
    def stop(self):
        self.change_x = 0
    # - END stop method

    # - Jump method
    def jump(self):
        # -- check whether the player is on the platform
        self.rect.y += 2 # -- set the rect.y to the current position + 2px
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_group, False) # -- check if we are on a platform
        self.rect.y -= 2 # -- set the rect.y to the current position - 2px

        # -- if the player sprite can jump, set the change_y
        if len(platform_hit_list) > 0:
            self.change_y = -10 # -- set change_y to -10
        # -- END IF
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
# - END CLASS

# - Platform CLASS
# -- attributes: 
class Level():
    # - Constructor method
    def __init__(self, player):
        self.platform_group = pygame.sprite.Group() # -- creating a new platform_group
        self.player = player # -- assigning the Player object to player
        self.world_shift = 0 # -- set the world_shift to 0
    # - END Constructor method

    # - Update method
    def update(self):
        self.platform_group.update() # -- update everything in the level
    # - END Update method

    # - Draw method
    def draw(self, screen):
        self.platform_group.draw(screen) # -- draw all of the sprites on the screen
    # - END Draw method
    
    # - Shift_world method
    def shift_world(self, shift_x):
        self.world_shift += shift_x # -- increment the world_shift variable
 
        # -- go through all the platforms in the platform_group,
        for platform in self.platform_group:
            platform.rect.x += shift_x # -- set the rect.x to rect.x + shift_x#
        # -- END for
    # - END Shift_world method
# - END CLASS

# - Platform CLASS
# -- attributes: Level
class Level_01(Level):
    # - Constructor method
    def __init__(self, player):
        Level.__init__(self, player) # -- call the parent constructor
        self.level_limit = -1000 # -- set the level_limit to -1000
 
        # -- Level platforms
        # -- width, height, x and y-coordinates of the platform
        level = [
            [300, 30, 200, 350],
            [300, 30, 100, 250],
            [300, 30, 400, 550],
            [300, 30, 650, 500],
            [300, 30, 400, 400],
            [300, 30, 820, 300],
        ]

        # -- loop through all of the platforms in the level list
        for platform in level:
            block = Platform(platform[0], platform[1], platform[2], platform[3]) # -- create an instance of a Platform, and pass in the parameters from the list array
            block.player = self.player # -- set block.player to the player object
            self.platform_group.add(block) # -- add the block to the platform_group
        # - END FOR
    # - END Constructer method
# - END CLASS

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

    player = Player() # -- create an instance of the Player class

    level_list = [] # --level_list array
    level_list.append(Level_01(player)) # -- add the instance of Level_01(player) to the level_list array
 
    current_level_no = 0 # -- set the current_level_no to 0
    current_level = level_list[current_level_no] # -- get the current level value from the level_list array
 
    active_sprite_list = pygame.sprite.Group() # -- create an active_sprite_list sprites group
    player.level = current_level # -- set the player level to the current level

    active_sprite_list.add(player) # -- add the instance of player to the active_sprite_list

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
            # -- if the user quits the game
            if event.type == pygame.QUIT:
                running = False # -- set the variable running to False
            # - END IF

            # -- if a key is pressed
            if event.type == pygame.KEYDOWN:
                # -- if an escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    running = False # -- set running to false
                # -- END IF
                # -- if the user holds the left key
                if event.key == pygame.K_LEFT:
                    player.move_left() # -- run the move_left() method
                # -- END IF
                # -- if the user holds the right key
                if event.key == pygame.K_RIGHT:
                    player.move_right() # -- run the move_right() method
                # -- END IF
                # -- if the user holds the up key
                if event.key == pygame.K_UP:
                    player.jump() # -- run the jump() method
                # -- END IF
            # - END IF

            # - if the user stops holding a key
            if event.type == pygame.KEYUP:
                # -- if the user lets go of the left key, and the change_x is less than 0
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop() # -- run the stop method
                # -- END IF
                # -- if the user lets go of the right key, and the change_y is greater than 0
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop() # -- run the stop method
                # -- END IF
            # - END IF

            # -- if he user clicks with the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # -- if it's a left click
                if event.button == 1:
                    click = True # -- set the variable click to true
                # - END IF
            # - END IF
        # - END FOR

        active_sprite_list.update() # -- update the sprites in active_sprite_list
        current_level.update() # -- update items in the current_level
 
        # -- if the player gets near the right side, shift the world left (by -x)
        if player.rect.right >= 680:
            difference = player.rect.right - 680 # -- calculate the difference
            player.rect.right = 680 # -- set the player.rect.left to 680
            current_level.shift_world(-difference) # -- shift the world by the difference
        # - END IF

        # -- if the player gets near the left side, shift the world left (by +x)
        if player.rect.left <= 120:
            difference = 120 - player.rect.left # -- calculate the difference
            player.rect.left = 120 # -- set the player.rect.left to 120
            current_level.shift_world(difference) # -- shift the world by the difference
        # - END IF
 
        current_position = player.rect.x + current_level.world_shift # -- set the current_position to player's rect.x + the current world_shift value
        # -- if the player gets to the end of the level, to to the next level
        if current_position < current_level.level_limit:
            player.rect.x = 120 # -- set the rect.x value
            # -- if the current_level_no is lower than the length of the list - 1,
            if current_level_no < len(level_list) - 1:
                current_level_no += 1 # -- increment the level_no by 1
                current_level = level_list[current_level_no] # -- get the current level value from the level_list array
                player.level = current_level # -- set player.level to the current_level
            # - END IF
        # - END IF
 
        current_level.draw(screen) # -- draw the current level on the screen
        active_sprite_list.draw(screen) # -- draw sprites in the active_sprite_list on the screen

        pygame.display.update() # -- update the display
        fpsClock.tick(FPS) # -- set the display to 60fps
    # - END WHILE
    pygame.quit() # -- quit the game
# - END FUNCTION

main_menu() # -- calling the main_menu function, so that it's the first executed