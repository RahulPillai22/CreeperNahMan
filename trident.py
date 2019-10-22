import pygame
from pygame.sprite import Sprite
# When we use sprite we can group related elements in our game and act on all the group elements at once such as the tridents

class Trident(Sprite):#Trident class inherits from Sprite which we have imported from pygame.sprite module

    # A class to manage the tridents being shot by the pewds model
    def __init__(self,cNM_S,screen,pewdsModel):
        #create a trident object at the pewds model's position
        super(Trident,self).__init__()#To inherit from Sprite
        self.screen=screen

        self.image=pygame.image.load('C:\\Users\\Rahul Pillai\\Desktop\\_\\College\\SkillShare\\PythonGameDevelopment\\Codes\\CreeperNahMan\\CreeperNahMan\\CreeperNahMan\\ImageAssets\\Trident.png')
        self.rect=self.image.get_rect()
        #self.rect=pygame.Rect(0,0,cNM_S.tridentWidth, cNM_S.tridentHeight) #not using this
        #Set the correct position of the trident rectangle as the same position as that of pewds model
        self.rect.centerx = pewdsModel.rect.centerx
        #self.rect.top = pewdsModel.rect.top#If we want the trident to shoot from inside the pewds model
        self.rect.bottom = pewdsModel.rect.centery#If we want the trident to shoot from middle part of the pewds model

        # Store the trident's position as a decimal value
        self.y = float(self.rect.y)
        #self.color = cNM_S.tridentColor
        self.speed = cNM_S.tridentSpeed
    
    def update(self):
        #Move the trident up the screen
        #Update the decimal position of the trident
        self.y-=self.speed # as trident moves up the screen we need to decrease its y coordinate value depending on the speed
        #update the rect position
        self.rect.y = self.y

    def drawTrident(self):
        # Draw the trident to the screen
        self.screen.blit(self.image,self.rect)#inside the bracket the arguments go as (source(pygame surface which in this case is the image),destination)


