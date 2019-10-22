#class to store settings:
class Settings():
    def __init__(self):
        self.screen_width=1280
        self.screen_height=720
        #self.bg_color=(50,200,155) #commented since we are using a background image (See the main file GameStructure.py)
        
        #pewds model settings
        self.pewdsModelsLimit=3 #Meaning we get 3 lives

        #creeperCollection settings
        self.creeperCollectionDropSpeed=10
        
        #How quickly the game speeds up
        self.speedupScale = 1.2

        #How quickly the creeper point value increases
        self.scoreScale = 1.5

        self.initializeDynamicSettings()

    def initializeDynamicSettings(self):
        #Initialize settings that change during the game
        #We will increase speeds of pewdsModel, tridents and creepers as the player progresses through the game and reset them each time the player starts a new game.

        #pewds model settings
        self.modelSpeed=5

        #Trident settings (Projectile to be shot at enemy)
        self.tridentSpeed=8

        #Creeper settings
        self.creeperSpeedFactor=5
    
        #creeperCollectionDirection = 1 represents right, -1 rperesents left
        self.creeperCollectionDirection = 1
        #creeperCollectionDirection is included in this function so that each time the game resets or starts the creeperCollection moves to the right

        #Scoring
        self.creeperPoints = 100#Reset points alloted to each creeper, each time the game starts/restarts

    def increaseSpeed(self):
        #Increase speed settings and creeper point value
        self.modelSpeed *= self.speedupScale
        self.tridentSpeed *= self.speedupScale
        self.creeperSpeedFactor *= self.speedupScale

        self.creeperPoints = int(self.creeperPoints * self.scoreScale)