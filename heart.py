import pygame
from pygame.sprite import Sprite

class Hearts(Sprite):
    def __init__(self,cNM_S,screen):
        #Initialize our Heart/Health model and set its starting position
        super(Hearts, self).__init__()

        #Load the heart's image
        self.image=pygame.image.load('C:\\Users\\Rahul Pillai\\Desktop\\_\\College\\SkillShare\\PythonGameDevelopment\\Codes\\CreeperNahMan\\CreeperNahMan\\CreeperNahMan\\ImageAssets\\Heart.png')
  
        self.rect=self.image.get_rect()
