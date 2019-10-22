import pygame
from pygame.sprite import Sprite

class Pewds(Sprite):
    def __init__(self,cNM_S,screen):
        #Initialize our Pewdiepie model and set its starting position
        super(Pewds, self).__init__()
        self.screen=screen
        self.cNM_S=cNM_S

        #Load the Pewdiepie model image
        self.image=pygame.image.load('C:\\Users\\Rahul Pillai\\Desktop\\_\\College\\SkillShare\\PythonGameDevelopment\\Codes\\CreeperNahMan\\CreeperNahMan\\CreeperNahMan\\ImageAssets\\PewdsMinecraft.png')
        #above function returns a surface representing a Pewdiepie model which we store in self.image
        
        #if we needed to scale the image we would use below 2 line
        #self.imageScaled=pygame.transform.scale(self.image,(100,100))
        #self.rect=self.imageScaled.get_rect() 
        
        self.rect=self.image.get_rect()
        #to access the surface rect attribute, python lets you treat elements as rectangles
        # even if they are not shaped as rectangles because rectangles are simple shapes to work with
        self.screenRect=screen.get_rect()

        #when using a rect object we can use the x and y coordinates of the top, bottom, left and right edges of the rectangle as well as the center
        #we can set any of these values to determine the current position of the rect

        #Start each new Pewdiepie model at bottom-middle of the screen
        self.rect.centerx=self.screenRect.centerx # matching the x coordinate of Pewdiepie model's center with the centerx attribute of the screenRect
        self.rect.bottom=self.screenRect.bottom # matching the y coordinate of Pewdiepie model's bottom with the bottom attribute of screenRect

        #Storing a decimal value for the pewds model's center
        self.center = float(self.rect.centerx)

        # Movement flag for continuous movement of pewds model when key is pressed down
        self.movingRight=False
        self.movingLeft=False

    def update(self):
        #update the model's position based on the movement flag
        if self.movingRight and self.rect.right < self.screenRect.right:# statement after and is to prevent model from going beyond the 
            # far right of the screen, self.rect.right is the x coordinate of the right edge of the pewds model's rectangle, self.screenRect.right
            # is the x coordinate of the right edge of the screen
            self.center+=self.cNM_S.modelSpeed
        if self.movingLeft and self.rect.left > 0:# statement after and is to prevent model from going beyond the far left of the screen
            #self.rect.left is the x coordinate of the left edge of the pewds model's rectangle, 0 is the x coordinate of the left edge of the screen
            self.center-=self.cNM_S.modelSpeed

        #update rect object from self.center
        self.rect.centerx=self.center

    def blitme(self):
        #Draw the Pewdiepie model at its current location
        self.screen.blit(self.image,self.rect)

    def centerPewdsModel(self):
        #Center the pewdsModel on the screen
        self.center  = self.screenRect.centerx #Set the center of the pewdsModel to match the center of the screen