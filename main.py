import random # for generating of the random  numbers
import sys    # for the exit the programme
import pygame # for the pygame module
from pygame.locals import * # Pygame special Variables


# Declearing the Global Variables

FPS = 32
SCREENWIDTH = 289
SCREENHIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHIGHT))
GROUNDY = SCREENHIGHT * 0.8
GAME_IMAGES = {} # All the game images in the Gallary folder 
GAME_SOUNDS = {} # All the Audio of the game in the gallary folder 
PLAYER = 'Gallary/images/bird.png'
BACKGROUND = 'Gallary/images/background.png'
PIPE = 'Gallary/images/bamboo.png'

# Definig the functions

def welcomescreen():
    """
    This is the Welcome screen shows to the User.
    """
    playerx = int(SCREENWIDTH / 5) # x cordinate of the player
    playery = int((SCREENHIGHT - GAME_IMAGES['player'].get_height()) / 2) # y cordinate of the bird, and to center the image. 
    messagex = int((SCREENWIDTH - GAME_IMAGES['message'].get_width()) / 2) # show the message position at the x cordinate
    messagey = int(SCREENHIGHT * 0.13)
    basex = 0
    while True:
        # This will tell the user about their input they performed with the mouse or keyboard.
        for event in pygame.event.get():
            # if the user input the cross or ese key the game will stop.
            # for more about keys google pygame keys

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # if the user enter  space or the arrow key, start the game for them

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP ):
                return
            else:
                # now we will bilt the images it takes images and cordianates 
                SCREEN.blit(GAME_IMAGES['background'], (0, 0))
                SCREEN.blit(GAME_IMAGES['player'], (playerx, playery))
                SCREEN.blit(GAME_IMAGES['message'], (messagex, messagey))
                SCREEN.blit(GAME_IMAGES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)










if __name__ == '__main__':
    # This is the main body of the function
    pygame.init() # initializing the pygame function.
    FPSCLOCK = pygame.time.Clock() # for controlling the frames of the Game 
    pygame.display.set_caption('Flappy Bird By Shubhajit') # initializing the name of the Game 
    #set the dictionary for the game images, keys are the name and values are the relative path of that image.
    GAME_IMAGES['numbers'] = (
        pygame.image.load('Gallary/images/0.png').convert_alpha(),
        pygame.image.load('Gallary/images/1.png').convert_alpha(),
        pygame.image.load('Gallary/images/2.png').convert_alpha(),
        pygame.image.load('Gallary/images/3.png').convert_alpha(),
        pygame.image.load('Gallary/images/4.png').convert_alpha(),
        pygame.image.load('Gallary/images/5.png').convert_alpha(),
        pygame.image.load('Gallary/images/6.png').convert_alpha(),
        pygame.image.load('Gallary/images/7.png').convert_alpha(),
        pygame.image.load('Gallary/images/8.png').convert_alpha(),
        pygame.image.load('Gallary/images/9.png').convert_alpha(),
    )

    GAME_IMAGES['message'] = pygame.image.load('Gallary/images/welcome.png').convert_alpha()
    GAME_IMAGES['base'] = pygame.image.load('Gallary/images/ground.png').convert_alpha()
    GAME_IMAGES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), # for the 180 rotation of pipe
        pygame.image.load(PIPE).convert_alpha()
        )
    GAME_IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_IMAGES['player'] = pygame.image.load(PLAYER).convert_alpha()

    #set the Dictionary for the game sounds.
    # GAME_SOUNDS[] which i have to  downlode.




    # Starting the Game Loop of the program

    while True:
        welcomescreen() #Shows the welcome screen until the user press a button 
        maingame() # This is the main function for running of the Game




