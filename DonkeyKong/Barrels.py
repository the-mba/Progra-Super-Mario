from Ladders import Ladders
from Broken_Ladders import Broken_Ladders
import random
class Barrels:
    def __init__(self):
        self.ladders = Ladders() #importing the ladders to make barrels fall through them
        self.Bladders = Broken_Ladders() #importing the broken ladders to make barrels fall through them
        self.positionx = 0 #initial x position of the barrels
        self.positiony = 35 #initial y position of the barrels
        self.speed = 2 #horizontal speed of the barrels 
        self.platforms = True #Boolena used to check if the barrel is on a platform
        self.InitX = 0  #coordinates for the sprite selection
        self.InitY = 16  #coordinates for the sprite selection
        self.FinalX = 14  #coordinates for the sprite selection
        self.FinalY = 16  #coordinates for the sprite selection
        self.laddersX = self.ladders.LaddersX + self.Bladders.bladdersX #changing the name of the list with the coordinates
        self.laddersY = self.ladders.LadderY + self.Bladders.bladdersY #changing the name of the list with the coordinates
    def moving(self):
        '''In this method we move the barrels to the left or to the right depending on which platform 
        they are in, then we make them have a 25% chance (1 in 4) of falling through a ladder (broken or not). 
        Then we implement the "gravity" by making the barrels fall if they are nou in a platform until they reach one, 
        this makes them fall trough ladders as well because we say taht if the 25% chance turns up in a ladder, 
        that barrel is no longer in a platform, so it falls. Finally we make them reappear at the end when they fall 
        a certain distance instead of taking them out of the lsit, so less processing power is used'''
        if (self.positiony == 35 and self.positionx <= 220) or (self.positiony == 115  and self.positionx <= 220) or (self.positiony == 195 and self.positionx <= 220):
            self.positionx += self.speed
            self.platforms = True
        elif (self.positiony == 75 and self.positionx >= 20) or (self.positiony == 155 and self.positionx >= 20) or (self.positiony == 235 and self.positionx >= -20):
            self.positionx -= self.speed
            self.platforms = True
        else:
            self.platforms = False           
        for x in range(len(self.laddersX)):
            if self.laddersX[x] == self.positionx + 3 and (self.laddersY[x]-23) == self.positiony:
                y = random.randint(1,4)
                if y == 1:
                    self.platforms = False
        if self.platforms == False:
            self.positiony += 2.5
        if self.positiony > 300:
            self.positiony = 35
            self.positionx = 0
    def Painting(self):
        '''This method is similar to mario's one, if the barrel is not in a platform (gravity will make it fall) 
        we change the sprite, we also divide the x axis in sets of 4 and for each pyxel in that block we have a 
        different sprite so that there is an illusion of rolling'''
        if self.platforms == False:
            self.InitX = 48
            self.InitY = 0
            self.FinalX = 16
        else:
            if self.positionx %16 == 0:
                self.InitX = 0
                self.InitY = 16
                self.FinalX = 14
                self.FinalY = 16
            elif self.positionx %16 == 4:
                self.InitX = 32
                self.InitY = 80 
            elif self.positionx %16 == 8:
                self.InitX = 0
                self.InitY = 80 
            elif self.positionx %16 == 12:
                self.InitX = 48
                self.InitY = 80 
                
    def update(self):
        self.moving()
        self.Painting()
                
                