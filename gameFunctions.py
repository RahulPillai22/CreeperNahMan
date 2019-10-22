import sys
from time import sleep #Since when a collision of pewdsModel and creeper happens we need to pause for some time to allow the player to regroup before the new
# creeper collection appears
import pygame
from trident import Trident
from creeper import Creeper


def checkKeydownEvents(event,cNM_S,screen,pewdsModel,tridents):
    #Respond to key presses
    if event.key == pygame.K_RIGHT:
        #Move the Pewdiepie model to the right
        pewdsModel.movingRight=True# setting the movement flag to True to start moving the pewds model right
    elif event.key == pygame.K_LEFT:
        pewdsModel.movingLeft=True
    elif event.key == pygame.K_SPACE:
        #Create a new trident and add it to the tridents group
        newTrident=Trident(cNM_S,screen,pewdsModel)
        tridents.add(newTrident)#To add a new trident to the tridents group
    

def checkKeyupEvents(event,pewdsModel):
    #Respond to key-up / key releases
    if event.key == pygame.K_RIGHT:
        pewdsModel.movingRight=False
        #what we did is if the right key is no longer pressed down then we set the movement flag to False to stop moving the pewds model right
    elif event.key == pygame.K_LEFT:
        pewdsModel.movingLeft=False


def checkEvents(cNM_S, screen, stats, sb, playButton, pewdsModel, creepers, tridents):
    #Respond to key presses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:#When any key is pressed down call the checkKeydownEvents function
            checkKeydownEvents(event,cNM_S,screen,pewdsModel,tridents)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event,pewdsModel)
        elif event.type == pygame.MOUSEBUTTONDOWN:#Mouse button down is detected when we click anywhere on the screen
            mouseX, mouseY = pygame.mouse.get_pos()# A tuple containing the x and y coordinates of mouse cursor is returned when mouse button is clicked
            checkPlayButton(cNM_S, screen, stats, sb, playButton, pewdsModel, creepers, tridents, mouseX, mouseY)#We want to respond to mouse clicks only on the play button

def checkPlayButton(cNM_S, screen, stats, sb, playButton, pewdsModel, creepers, tridents, mouseX, mouseY):
    #Start a new game when the Play Button is clicked
    buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
    if buttonClicked and not stats.gameActive: #Does point of mouse click overlap with the region defined by the rect of the play button and the game hasn't started yet     
        
        #Reset the game settings
        cNM_S.initializeDynamicSettings()

        #Hide the mouse cursor
        pygame.mouse.set_visible(False)
        
        #Reset the game stats
        stats.resetStats()# We give the player 3 new pewdsModels
        stats.gameActive = True #The game goes into active state i.e. it begins

        #Reset the scoreboard images
        sb.prepScore()
        sb.prepHighScore()
        sb.prepLevel()
        sb.prepHearts()

        #Empty the list of creepers and tridents
        creepers.empty()
        tridents.empty()

        #Create a new creeper collection and center the pewdsModel
        createCreeperCollection(cNM_S, screen, pewdsModel, creepers)
        pewdsModel.centerPewdsModel

def updateScreen(cNM_S, screen, stats, sb, pewdsModel, tridents, creepers, playButton):
    #update the images on the screen and filp to the new screen
    #Redraw all the tridents behind the pewds model and the creepers.
    for trident in tridents.sprites():# trident.sprites() returns a list of all sprites in the group tridents
        trident.drawTrident()

    pewdsModel.blitme()#This is called after filling the background since we want the Pewdiepie model to appear on the top of the background and not beneath it
    #Redraw the screen during each pass through the loop

    creepers.draw(screen)#To draw the group of creepers 

    #Now when we call draw on a group (in this case creepers) pygame automatically draws each element in the group at the position
    # defined by its rect attribute

    #Draw the score info
    sb.showScore()

    #Draw the "Play" button if the screen is inactive
    if not stats.gameActive:
        playButton.drawButton()#To make the play button visible above all our other elements on the screen we draw it after all the other game elements.

    #screen.fill(cNM_S.bg_color) #commented since we are using a background image (See the main file GameStructure.py)


    #make the most recently drawn screen visible
    pygame.display.flip()# this call will constantly update our display to show the new positions of the elements and hide the old ones.

def updateTridents(cNM_S, screen, stats, sb, creepers, pewdsModel, tridents):
    #Update position of tridents and remove old tridents
    
    #Update trident positions
    tridents.update()

    #Remove tridents that have gone off game screen
    for trident in tridents.copy(): # a copy is made since we shouldn't remove items from a list or a group in a for loop soo we have to  loop
        # over a copy of the group, we use the copy method to set up the for loop which enables us to modify the tridents inside the loop
        if trident.rect.bottom <=0:
            tridents.remove(trident)

    checkTridentCreeperCollisions(cNM_S, screen, stats, sb, pewdsModel, creepers, tridents)

def checkTridentCreeperCollisions(cNM_S, screen, stats, sb, pewdsModel, creepers, tridents):
    #Respond to trident-creeper collisions    
    #Check for any tridents that have hit creepers.
    #Get rid of that trident and that creeper
    collisions = pygame.sprite.groupcollide(tridents, creepers, True, True)
    #Above line loops through each trident in the group tridents and then loops through each creeper in the group creepers, whenever the rectangles of a trident and a 
    # creeper overlap then groupcollide adds a key:value pair to the dictionary it returns, the 2 True arguments tell pygame whether to delete the tridents and the
    # creepers that have collided

    for creepers in collisions.values():#When trident hits a creeper pygame returns a dictionary in the collisions variable and each value in the dictionary is a list 
        # of creepers hit by a single trident
        stats.score += cNM_S.creeperPoints * len(creepers) # if dictionary exists then we add the multiplication of the points value of each creeper to the 
        # number of creepers in each list, to the score
        sb.prepScore()#To create a new image for the updated score
    checkHighScore(stats, sb)

    if len(creepers)  == 0: #If the group of creepers is empty
        #If the creeperCollection is destroyed then move up one level
        tridents.empty()#Destroy existing tridents, The empty method removes all the remaining sprites from a group
        cNM_S.increaseSpeed()#Speedup the game

        #Increase level
        stats.level += 1
        sb.prepLevel()

        createCreeperCollection(cNM_S,screen,pewdsModel,creepers)#Create a new creeperCollection


def createCreeperCollection(cNM_S,screen,pewdsModel,creepers):
    #Create a collection of creepers
    #Create a creeper and find the number of creepers in a row.
    creeper=Creeper(cNM_S,screen) #creeper is object of Creeper class
    numberCreeperX = getNumberCreepersX(cNM_S,creeper.rect.width)
    numberRows= getNumberRows(cNM_S,pewdsModel.rect.height,creeper.rect.height)
    
    #Create a collection of creepers
    for rowNumber in range(numberRows):#We created a nested for loop to create rows the outer for loop decides no of rows and inner for loop decides no of 
        # creeper in each row
        for creeperNumber in range(numberCreeperX):
            #Create a creeper and place it in the row
            createCreeper(cNM_S,screen,creepers,creeperNumber,rowNumber)


def getNumberCreepersX(cNM_S,creeperWidth):
    #How many creepers can fit in a row
    availableSpace=cNM_S.screen_width - (2* creeperWidth)
    numberCreepersX=int( availableSpace / (3*creeperWidth))#numberCreepersX is the number of creepers in one row
    #(3*creeperWidth) since a creeper has its own width that is 1 creeperWidth and we have kept an empty space next to it of same width as twice of itself
    # i.e. 2 creeperWidth so, total 1+2 =3creeperWidth
    return numberCreepersX

def createCreeper(cNM_S,screen,creepers,creeperNumber,rowNumber):
    #Create a creeper and place it in a row
    #Spacing between creepers is equal to one creeper width
    creeper= Creeper(cNM_S,screen)
    creeperWidth=creeper.rect.width
    creeper.x= 1*creeperWidth + (3*creeperWidth*creeperNumber) #creeperWidth is added since each creeper is pushed to the right by 1 creeperWidth (to get correct 
    # available space on screen) from the left margin and the (3*creeperWidth*creeperNumber) is to account for the space that each creeper 
    # takes up that is 1 creeperWidth and we have kept an empty space next to it of same width as twice of itself i.e. 2 creeperWidth so, total 1+2 =3creeperWidth
    creeper.rect.x=creeper.x
    creeper.rect.y=creeper.rect.height + 1.5 * creeper.rect.height * rowNumber #Setting the y-coordinate of each row of creepers, creeper.rect.height is added since we 
    # leave space equal to 1 creeperHeight from the top and then we add  1.5 * creeper.rect.height * rowNumber since each creeper row is of height 1 creeperHeight
    # and we leave a space of 0.5 creeperHeight below each row
    creepers.add(creeper)

def getNumberRows(cNM_S,pewdsModelHeight,creeperHeight):
    #Determine the number of rows of creepers that fit on the screen
    availableSpaceY= (cNM_S.screen_height - (3* creeperHeight)- pewdsModelHeight)# 1 creeperHeight space is left empty from top of the screen and then we subtract the
    # pewdsModel's height from bottom and then above the model 2 creeperHeight of space is left empty so that we have some time to shoot the tridents before the creepers
    #start coming down hence we subtract ((3* creeperHeight)- pewdsModelHeight) from screen_height
    numberRows=int(availableSpaceY/ (2* creeperHeight)) # (2* creeperHeight) since 1 row is of 1 creeperHeight and below each row we leave space equal to 1 creeperHeight
    # before the next row
    return numberRows

def checkCreeperCollectionEdges(cNM_S, creepers):
    #Respond if any creepers have reached the edge of the screen
    for creeper in creepers.sprites():#Looping through all the creepers
        if creeper.checkEdges():
            changeCreeperCollectionDirection(cNM_S, creepers)#If a creeper has reached the edge of the screen then the whole creeperCollection needs to change direction
            break

def changeCreeperCollectionDirection(cNM_S, creepers):
    #Drop the creeperCollection and change the creeperCollection's  direction
    for creeper in creepers.sprites():#Looping through all the creepers
        creeper.rect.y += cNM_S.creeperCollectionDropSpeed #Drop each creeper down by  value of creeperCollectionDropSpeed (This value is  stored in Settings.py)
    cNM_S.creeperCollectionDirection *= -1

def pewdsModelHit(cNM_S, stats, sb, screen, pewdsModel, creepers, tridents):
    #Respond to a pewdsModel being hit by a creeper
    if stats.pewdsModelsLeft > 0:#If the player has at least 1 pewdsModel left then we create a new creeperCollection and then pause and move on
        #Decrement pewdsModelsLeft
        stats.pewdsModelsLeft -= 1

        #Update scoreboard
        sb.prepHearts()#Correct number of hearts are displayed each time a pewds model is destroyed

        #Empty list of creepers and tridents
        creepers.empty()
        tridents.empty()

        #Create a new creeperCollection and center the pewdsModel
        createCreeperCollection(cNM_S, screen, pewdsModel, creepers)
        pewdsModel.centerPewdsModel()

        #Pause
        sleep(0.5)#We pause after all the updates above have been made to the game elements but before any of the changes have been drawn to the screen, so the player can
        # see that the pewdsModel has been hit
    else:
        stats.gameActive = False #If player has used up all the pewdsModels then we set gameActive flag to False
        pygame.mouse.set_visible(True)

def checkCreepersBottom(cNM_S, stats, sb, screen, pewdsModel, creepers, tridents):
    #Check if the creepers have reached the bottom of the screen
    screenRect = screen.get_rect()
    for creeper in creepers.sprites():
        if creeper.rect.bottom >= screenRect.bottom:#To check if the bottom of the creeper has reached or gone beyond the bottom of the screen
            #Treat this the same as if the pewdsModel got hit
            pewdsModelHit(cNM_S, stats, sb, screen, pewdsModel, creepers, tridents)
            break#If one creeper hits the bottom of the screen then there is no need to check for the rest of the creepers and thus we break out

def updateCreepers(cNM_S, stats, screen, sb, pewdsModel, creepers, tridents):
    #Check if the creeperCollection has reached the edge and then update the position of all creepers
    checkCreeperCollectionEdges(cNM_S,creepers)# To check if any creepers have reached the edge of the screen
    creepers.update()

    #Look for creeper-pewdsModel collisions
    if pygame.sprite.spritecollideany(pewdsModel, creepers):#The method spritecollideany takes 2 arguments a sprite and a group, this method looks for any member of
        # the group that has collided with the sprite and stops looking through the group as soon as it finds one member that has collided with a sprite, in this case 
        # it loops through the group creepers and finds the 1st creeper that has collided with the sprite i.e. pewdsModel, if there is no collision then spritecollideany 
        # returns none and the if block wont execute but if it finds a creeper that has collided with pewdsModel then spritecollideany returns that creeper sprite from 
        # the creepers group and the if block executes
        pewdsModelHit(cNM_S, stats, sb, screen, pewdsModel, creepers, tridents)
    
    #Look for creepers hitting the bottom of the screen
    checkCreepersBottom(cNM_S, stats, sb, screen, pewdsModel, creepers, tridents)

def checkHighScore(stats, sb):
    #Check to see if there is a new high score.
    if stats.score > stats.highScore:
        stats.highScore = stats.score
        sb.prepHighScore()#To prepare new high score image/ to update high score image

