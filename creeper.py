import pygame
from pygame.sprite import Sprite

class Creeper(Sprite):
    #A class to represent a single creeper

    def __init__(self,cNM_S,screen):
        #Initialize the creeper and its starting position
        super(Creeper,self).__init__()
        self.screen=screen
        self.cNM_S=cNM_S

        #Load the creeper image and set its rectangle
        self.image = pygame.image.load('C:\\Users\\Rahul Pillai\\Desktop\\_\\College\\SkillShare\\PythonGameDevelopment\\Codes\\CreeperNahMan\\CreeperNahMan\\CreeperNahMan\\ImageAssets\\Creeper.png')
        self.rect=self.image.get_rect()

        #Start each new creeper near top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Adding space above the creeper equal to its height and space to the left of the creeper equal to its width
        #Store the creepers' exact position
        self.x = float(self.rect.x)

    def blitme(self):
        #Draw the creeper at its current position
        self.screen.blit(self.image, self.rect)

    def checkEdges(self):
        #Return true if creeper is at the edge of the screen
        screenRect= self.screen.get_rect()
        if self.rect.right >= screenRect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #Move the creepers to the right or left
        self.x += (self.cNM_S.creeperSpeedFactor * self.cNM_S.creeperCollectionDirection)# if creeperCollectionDirection = 1 the creeperCollection moves to
        #the right and if creeperCollectionDirection = -1 then the creeperCollection moves to the left
        self.rect.x = self.x
