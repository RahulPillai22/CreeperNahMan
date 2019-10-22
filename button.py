import pygame.font #To render text  to the screen
class Button():

    def __init__(self, cNM_S, screen, msg):
        #Initialize button attributes
        self.screen = screen
        self.screenRect = screen.get_rect()

        #Load the image for the play button
        self.image=pygame.image.load('C:\\Users\\Rahul Pillai\\Desktop\\_\\College\\SkillShare\\PythonGameDevelopment\\Codes\\CreeperNahMan\\CreeperNahMan\\CreeperNahMan\\ImageAssets\\PlayButton.png')

        #Build the button's rect object and center 
        self.rect=self.image.get_rect()
        self.rect.center = self.screenRect.center

    def drawButton(self):
        #Draw the button to the screen
        self.screen.blit(self.image,self.rect)

        




