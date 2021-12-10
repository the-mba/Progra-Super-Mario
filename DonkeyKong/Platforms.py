class Platforms:
    def __init__(self):
        self.positionx = 0 # the x is 0 because it is modified in the draw method of the board
        self.positiony = [20,45,85,125,165,205,245] #list with all the y coordinates of the platforms
        self.InitX = 0 #coordinates for the sprite selection
        self.InitY = 32 #coordinates for the sprite selection
        self.FinalX = 32 #coordinates for the sprite selection
        self.FinalY = 16 #coordinates for the sprite selection
    