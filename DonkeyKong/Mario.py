from Ladders import Ladders
from Pauline import Pauline
class Mario:

    def __init__(self, lives : int = 3, Score : int = 0):
        self.x = 2.75 #position in x, it is also used as starting position
        self.y = 233 #position in y, it is also used as starting position
        self.__speed = 2.75 #speed of mario, how many pyxels does he move in the x axis in one frame 
        self.lives = lives #starting amount of lives
        self.jump = False #Boolean that checks if mario is jumpin, or not. By jumping I mean in the air and going upwards
        self.space = False #Boolean used to check when the user has pressed the space
        self.image = "standing_right" #String used to change sprites to give the sensation of movement
        self.state = 'still' #String used to see if mario  is moving to the right to the left or is still
        self.jumpspeed = 5 #like the normal speed but in the y axis and only makes mario go upwards
        self.max_counter = 5 #the maximum amount the jump counter can be, we use it to adjust the seconds mario is going to spend in the air
        self.gravity = 2.5 #like the jumpspeed but to make mario go downwards
        self.grav = False #Boolean used to check if mario is falling or not (mainly used to debug)
        self.jump_counter = 0 #integer used to stablish how much time is mario going to spend in the air
        self.ladder_jump = False #Boolean used to check if mario has jumped at the base of a ladder
        self.ladder = False #Boolean use dto check if mario is on a ladder 
        self.climb = False #String (False is just a placeholder) used to make mario go up or down in a stair 
        self.climbing = False #Boolean used to check if mario is climbing or not. By cimbing we mean that he is in a ladder and going upwards or downwards
        self.platform = False #Boolena used to check if mario is on a platform 
        self.climbspeed = 2.5 #The speed at wich mario climbs ladders
        self.InitX = 0 #Coordinate x of the top left corner of Mario's sprite in the sprites
        self.InitY = 0 #Coordinate y of the top left corner of Mario's sprite in the sprites
        self.FinalX = 16 #Coordinate x of the bottom right corner of Mario's sprite in the sprites
        self.FinalY = 16 #Coordinate x of the bottom right corner of Mario's sprite in the sprites
        self.previous = 'still' #String used to change the sprite the mario so that it looks that he runs 
        self.point = Score #Used to stablish Mario's score
        self.win = False
        self.Ladders = Ladders()
        self.pauline = Pauline()
        
    def drawing (self):
        
        '''This is a function which only purpose is to change marios sprite periodically depending on marios 
        position in the x axis if mario is moving in one direction we change the sprite to mario with the hands,
        then depending on the previous sprite used, we change the sprite to mario still loking right or left'''
        
        if self.state == 'moving_right' and self.x % 8.25 == 0:
            self.InitX = 16
            self.InitY = 0
        elif self.state == 'moving_right' and self.x % 8.25 != 0:
            self.InitX = 0
            self.InitY = 0
        if self.state == 'moving_left' and self.x % 8.25 == 0:
            self.InitX = 16
            self.InitY = 80
        elif self.state == 'moving_left' and self.x % 8.25 != 0:
            self.InitX = 48
            self.InitY = 16
        if self.state == 'still':
            if self.previous == 'moving_left':
                self.InitX = 48
                self.InitY = 16
            elif self.previous == 'moving_right':
                self.InitX = 0
                self.InitY = 0


    def movement(self):
        
        '''This method is used to move mario in the x axis, when an appropiate key is pressed, the main 
        program changes the state variable and the logic of moving mario is done here. Mario will move when
        a kay is pressed if: the key is a correct one and mario is not in a ladder and within the windows borders'''
        
#------------Movement in x--------------
        if self.state == 'moving_right' and not self.climbing and self.x < 241:
            self.x += self.__speed
            self.previous = 'moving_right'
        elif self.state == 'moving_left' and not self.climbing and self.x > 0:
            self.x -= self.__speed
            self.previous = 'moving_left'
#----------------------------------------

            

    def jumpscrpt(self):
        
        '''This method deals with the jump and gravity of mario, when the space key is pressed, the main program 
        turns the space variable into true, here all the confirmations are done and if mario is on a platform, and 
        the space key is pressed, the variable jump becomes tru and making use of a counter we add a certain ammount 
        (in this case substract) to the y coordinate of mario every frame, the number of frames specified by the 
        maximum counter and by how much we add to the counter each second'''
        
#-------------------Jump----------------
    
        if ((self.y == 33 and self.x < 220) or (self.y == 73 and self.x > 20) or (self.y == 113 and self.x < 220) or (self.y == 153 and self.x > 20) or (self.y == 193 and self.x < 220) or self.y == 233) or (self.y == 8 and self.x < 220 and self.x > 80) and not self.jump:
            self.platform = True
        else:
            self.platform = False
            
        if self.space and self.platform: 
            self.jump = True
            
        if self.jump and self.jump_counter <= self.max_counter:
            self.y -= self.jumpspeed
            self.jump_counter += 0.8
        elif self.jump_counter >= self.max_counter:
            self.jump = False
            self.jump_counter = 0
            
        if self.platform and self.ladder and self.space:
            self.ladder_jump = True
        elif self.ladder_jump and self.platform and not self.jump:
            self.ladder_jump = False
            
        #---------------Gravity--------------------
        if not self.platform and self.climb != 'up' and self.climb != 'down' and (not self.platform and not self.ladder or self.ladder_jump): 
            self.y += self.gravity
            self.grav = True
        else:
            self.grav = False
        #--------------------------------------
        
        
    def ladderscrpt(self):
        '''This method detects if mario is on a ladder adn is this is true and the playes presses one of the correct 
        keys, mario will go up or down the stairs, then we use a loop to check if mario is on top of a ladder and the 
        user still presses the up boton, the program will teletransport mario to the platform so that it does not look 
        as if mario is jumping, the same thing is done when mario is at the bottom of a ladder and the down boton is 
        pressed, the last part is to check if mario is climbing or not, mainly used to debug'''
    
        if (self.x <= 180 and self.x >= 170) and (self.y <= 233 and self.y >= 193) and not self.grav:#First Ladder
            self.ladder = True
        elif self.x <= 65 and self.x >= 50 and self.y <= 193 and self.y >= 153 and not self.grav:#Second Ladder
            self.ladder = True
        elif self.x <= 200 and self.x >= 190 and self.y <= 153 and self.y >= 113 and not self.grav:#Third Ladder
            self.ladder = True
        elif self.x <= 73 and self.x >= 60 and self.y <= 113 and self.y >= 73 and not self.grav:#Fourth Ladder
            self.ladder = True
        elif self.x <= 210 and self.x >= 200 and self.y <= 73 and self.y >= 33 and not self.grav:#Sixth Ladder
            self.ladder = True
        elif self.x <= 141 and self.x >= 133 and self.y <= 33 and self.y >= 4 and not self.grav:#Sixth Ladder
            self.ladder = True 
        else:
            self.ladder = False
            
        if self.climb == 'up' and self.ladder:
            self.y -= self.climbspeed
        if self.climb == 'down' and  self.ladder:
            self.y += self.climbspeed
            
        for x in range (len(self.Ladders.LaddersX)):
            if x%2 == 0 and self.climb == 'down':
                y= self.Ladders.LadderY[x]
                if self.y >= self.Ladders.LadderY[x] and self.y <= self.Ladders.LadderY[x]+3 and self.x <= self.Ladders.LaddersX[x]+12 and self.x >= self.Ladders.LaddersX[x]-12:
                    self.y = y
            if x%2 != 0 and self.climb == 'up':
                y = self.Ladders.LadderY[x]
                if self.y + 25 <= self.Ladders.LadderY[x] and self.y + 28 >= self.Ladders.LadderY[x] and self.x <= self.Ladders.LaddersX[x]+12 and self.x >= self.Ladders.LaddersX[x]-12:
                    self.y = y - 25
                else:
                    self.y = self.y
            if self.y <= 8 and self.y+10 <= 18:
                self.y = 8
        if self.ladder == True and not self.platform and not self.ladder_jump:
            self.climbing = True
        else:
            self.climbing = False
            
            
    def winscrpt(self):
        if self.x >= self.pauline.positionx and self.x <= self.pauline.positionx+16 and self.y == self.pauline.positiony+8:
            self.win = True
            
    def update(self):
        self.drawing()
        self.movement()
        self.jumpscrpt()
        self.ladderscrpt()
        self.winscrpt()
            


