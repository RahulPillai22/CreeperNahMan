import pygame
from pygame.sprite import Group
from heart import Hearts

class Scoreboard():
    #A class to store and show scoring info
    
    def __init__(self, cNM_S, screen, stats):
        #Initialize score attributes
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.cNM_S = cNM_S
        self.stats = stats
        

        #Font settings for score
        self.textColor = (235, 0, 55)
        self.font = pygame.font.SysFont("comicsansms", 25, bold = True, italic = True)

        #Prepare the inital score image
        self.prepScore()

        self.prepHighScore()# To prepare the high score image

        self.prepLevel()# To prepare the level image

        ##self.prepPewdsModels()
        self.prepHearts()

    def prepScore(self):
        #Turn the score into a rendered image
        roundedScore = int(round(self.stats.score, -1)) # round function normally rounds a decimal nonumber to a set number of decimal places given as the 2nd argument 
        # however if you pass a negative number as the 2nd argument, round will round the value to the nearest 10 ( for -1 ), or 100 ( for -2 ) or 1000 ( for -3 ) 
        # and so on.
        scoreStr = "SCORE "+"{:,}".format(roundedScore)# Format score with commas
        self.scoreImage = self.font.render(scoreStr, True, self.textColor, (0, 0, 0)) #To create an image out of a string, (0, 0, 0) is the colour of the game 
        # background we pass it to render to make the score appear more clearly on the screen

        #Display the score in the top right of the screen
        #We have the score expand to the left as the value of the score increases and the width of the number grows
        self.scoreRect = self.scoreImage.get_rect()#To make sure the score always lines up with right side of the screen we make a rect of the score image
        self.scoreRect.right = self.screenRect.right - 20#Set the right edge of the score rect 20 pixels from the right edge of the screen
        self.scoreRect.top = 1#Set the top edge of the score rect 4 pixels down from the top of the screen

    def showScore(self):
        #Draw the score, the high score and the current level to the screen
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.levelImage, self.levelRect)

        #Draw hearts
        self.hearts.draw(self.screen)

    def prepHighScore(self):
        #Turn the high score into a rendered image
        highScore = int(round(self.stats.highScore, -1))#Round the high score to the nearest 10
        highScoreStr = "HI-SCORE "+"{:,}".format(highScore)# Format high score with commas
        self.highScoreImage = self.font.render(highScoreStr, True, self.textColor, (0, 0, 0))#To create an image out of a string, (0, 0, 0) is the colour of the 
        # game background we pass it to render to make the high score appear more clearly on the screen

        #Center the high score at the top of the screen
        self.highScoreRect = self.highScoreImage.get_rect()# make a rect from the high score image
        self.highScoreRect.centerx = self.screenRect.centerx# center the high score rect horizontally
        self.highScoreRect.top = self.scoreRect.top# set the top of the high score as the top of the score image

    def prepLevel(self):
        #Turn the level into a rendered image
        levelStr = "LEVEL "+"{:,}".format(self.stats.level)
        self.levelImage = self.font.render(levelStr, True, self.textColor, (0, 0, 0))
        #self.levelImage = self.font.render(str(self.stats.level), True, self.textColor, (0, 0, 0))

        #Position the level below the score
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right#Set right of the level Rect to be same as the right of the score Rect
        self.levelRect.top = self.scoreRect.bottom + 1#Set the top of the level Rect to be  pixels below the bottom of the score Rect

    def prepHearts(self):
        #Show how many lives we have left
        self.hearts = Group()# An empty group is made to hold the instances of the hearts
        for heartNumber in range(self.stats.pewdsModelsLeft):#To fill the empty group, a for loop runs once for every model the player has left
            heart = Hearts(self.cNM_S, self.screen)#Create a new heart
            heart.rect.x = 10 + heartNumber * heart.rect.width#Set the heart's x coordinate such that the hearts appear next to each other with a 10 
            # pixel margin, on the left hand side of the group of hearts
            heart.rect.y = 7#We set the y coordinate to be 4 pixels down from the top of the screen so that the hearts line up with the score image.
            self.hearts.add(heart)#Finally we add each new heart to the group 
