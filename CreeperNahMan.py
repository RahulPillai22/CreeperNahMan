import sys # needed to exit the game when a player quits
import pygame
from pygame.sprite import Group
from Settings import Settings
from gameStats import GameStats
from scoreboard import Scoreboard
from button import Button
from pewds import Pewds
from creeper import Creeper
import gameFunctions as gf


def runGame():
    #initsialise game and create screen object
    pygame.init() #To initialise the background settings
    cNM_S=Settings()# object of the settings class cNM_S stands for "Creeper Nah Man! Settings"

    screen=pygame.display.set_mode((cNM_S.screen_width, cNM_S.screen_height)) # We create a display called screen, (1200,800) is a tuple which defines
    # the dimensions of the game window.
    # The screen object just created is called a surface
    # In pygame a surface is part of the screen where we display a game element,eg creeper will be a surface and the Pewdiepie model will be a surface in the game
    pygame.display.set_caption("Creeper Nah Man!")

    #Make a play button
    playButton = Button(cNM_S, screen, "Play")

    #Create an instance to store game stats and create a scoreboard
    stats = GameStats(cNM_S)
    sb = Scoreboard(cNM_S, screen, stats)

    #Make a Pewds model, a group of tridents and a group of creepers:-
    
    #Create a Pewdiepie model
    pewdsModel=Pewds(cNM_S,screen)# Creating an instance of Pewds class , this part is outside while since we do not want to create a new instance of Pewds class on each

    #Make a group to store tridents in
    tridents= Group()
    #The group is created outside the while loop so that we dont create a new group each time we pass through the while loop
    #This group will store all the live tridents so that we can manage the tridents that have already been fired by the user
    #This group will be an instance of the class pygame.sprite.Group, which behaves like a list with some extra functionality which is helpful when
    # building games, we will use this group to draw tridents on the screen on each pass through the main loop (while loop) and to update each tridents'
    # position

    #Make a group of creepers
    creepers=Group()

    #Create a collection of creepers
    gf.createCreeperCollection(cNM_S,screen,pewdsModel,creepers)
    
    #setting up backround image for the game
    bkgnd=pygame.image.load("C:\\Users\\Rahul Pillai\\Desktop\\_\\College\\SkillShare\\PythonGameDevelopment\\Codes\\CreeperNahMan\\CreeperNahMan\\CreeperNahMan\\ImageAssets\\bkgnd.png")
    #.convert() #convert is used since the image needs to be converted to a format Pygame can more easily work with.

    #set background color (Already done in Settings.py)
    #bg_color=(135,206,250) (Can use this if there was no Settings file)

    #start main loop for the game

    while True: # while loop that contains the game

        screen.blit(bkgnd, [0, 0]) # to set our background initially before everything
        # watch for keyboard and mouse events
        gf.checkEvents(cNM_S, screen, stats, sb, playButton, pewdsModel, creepers,  tridents) #this function exists in gameFunctions.py 
        #tridents is passed to this function since we need to check the event when space bar is pressed to shoot trident

        if stats.gameActive:
            pewdsModel.update()
        
            #tridents is passed to this function since we need to update the tridents drawn to the screen so we see the tridents moving up
            gf.updateTridents(cNM_S, screen, stats, sb, creepers, pewdsModel, tridents)# instead of doing tridents.update() and removal of off screen tridents here 
            # we have moved that code to a new function in gameFunctions.py
  
            gf.updateCreepers(cNM_S, stats, screen, sb, pewdsModel, creepers, tridents)
        
        gf.updateScreen(cNM_S, screen, stats, sb, pewdsModel, tridents, creepers, playButton)
    
  
runGame()


