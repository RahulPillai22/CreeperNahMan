class GameStats():
    #Track stats for CreeperNahMan
    def __init__(self, cNM_S):
        #Initialize stats
        self.cNM_S = cNM_S
        self.resetStats()

        #Start the game in an inactive state
        self.gameActive = False

        #High score should never be reset
        self.highScore = 0 #Since highScore should never be reset we initialize it in init function rather than in resetStats funtion

    def resetStats(self):
        #Initialize stats that can change during the game
        self.pewdsModelsLeft = self.cNM_S.pewdsModelsLimit
        self.score = 0 #At start of each game score is 0
        self.level = 1

       
