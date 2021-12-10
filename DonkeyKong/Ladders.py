class Ladders:
    def __init__(self,positionX: int = 0,positionY: int = 0):
        self.positionx = positionX
        self.positiony = positionY
        self.InitX = 34 #coordinates for the sprite selection
        self.InitY = 0 #coordinates for the sprite selection
        self.FinalX = 14 #coordinates for the sprite selection
        self.FinalY = 16 #coordinates for the sprite selection
        self.LaddersX = (180,180,60,60,200,200,70,70,210,210,86,86,86,86,76,76,76,76,140) #tuple with the x of all the ladders (each long ladder is composed of two sprites, thats why the tuples ar longer than expected)
        self.LadderY = (233,218,193,178,153,138,113,98,73,58,33,18,3,0,33,18,3,0,33) #tuple with the y of all the ladders (each long ladder is composed of two sprites, thats why the tuples ar longer than expected)
        