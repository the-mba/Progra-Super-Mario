import pyxel
from Static_Barrels import Static_Barrels
from Mario import Mario 
from Barrels import Barrels 
from DonkeyKong import DonkeyKong 
from Ladders import Ladders 
from Pauline import Pauline 
from Platforms import Platforms 
from Broken_Ladders import Broken_Ladders

        WIDTH = 256
        HEIGHT = 256

class Board:
    def __init__(self):
        self.Donkey = DonkeyKong()
        self.mario = Mario()
        self.Sbarrels = Static_Barrels()
        self.Mbarrels = Barrels()
        self.ladders = Ladders()
        self.Bladders = Broken_Ladders()
        self.platforms = Platforms()
        self.pauline = Pauline()
        self.donkeykong = DonkeyKong()

        self.state = 'Alive' #sting used to determine if mario is dead or alive

        CAPTION = "Super Mario Bros"
        pyxel.init(WIDTH, HEIGHT, caption = CAPTION, fps = 30)
        pyxel.load("assets/sprites.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        '''In this function we have implemented all the detections of the keyboard needed for the logic of mario 
        and the barrels, firstly we ran all the methods and then we implement two functionalities, if you press "Q" 
        the game ends and if you press "R" the game restarts. Then we change the state of mario depending on wether 
        you press te rigth arrow or the left or none of them, the same with the space, the same with the arrous UP 
        and DOWN for ladders, then we spawn barrels depending on the frame and they randomize with the ladders for 
        who they have a 25% chance of falling trhough'''
        self.mario.update()
        self.Mbarrels.update()
        self.Collisions()
        for barrel in self.barrels:
            barrel.Painting()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_R):
            self.state = 'Dying'
            self.mario.lives = 3
            self.mario.point = 0
        #------------------Mario Movement----------------------------
        else:
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                self.mario.state = 'moving_right'
            elif pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
                self.mario.state = 'moving_left'
            else:
                self.mario.state = 'still'
        #------------------------------------------------------------- 
        #----------------Jump-----------------------------------------   
            if pyxel.btn(pyxel.KEY_SPACE):
                self.mario.space = True
            else:
                self.mario.space = False
        #--------------------------------------------------------------
        #-----------------------------Climbing-------------------------
            if self.mario.ladder and (pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)):
                self.mario.climb = 'up'
            elif self.mario.ladder and (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)):
                self.mario.climb = 'down'
            else:
                self.mario.climb = False
        #--------------------------------------------------------------
        #------------------------Barrels-------------------------------
            if pyxel.frame_count % 100 == 0 and self.barrel_number <= 9:
                self.barrel_number += 1
            for x in range(self.barrel_number):
                self.barrels.append(())
                self.barrels[-1] = (Barrels())
                self.barrels[x].moving()

            if self.mario.x >= self.pauline.positionx-14 and self.mario.x <= self.pauline.positionx+12 and self.mario.y == self.pauline.positiony+8:
                self.mario.win = True
            else:
                self.mario.win = False
        #--------------------------------------------------------------
            
    def Collisions(self):
        '''If mario dies we empty the list of barrels so the disapear, if also mario has run out of lives, the program will 
        just turn off. If any part of mario touches a barrel, we substract one life from him and we reset his class so he 
        returns to the begining, but if mario jumps over a barrel we add 100 points, all accompanied by sounds'''
        if self.state == 'Dying' and self.mario.lives != 0:
            self.barrels = []
            self.barrel_number = 0
            self.mario = Mario(lives =self.mario.lives, Score = self.mario.point)
            self.state = 'Alive'
        if self.state == 'Dying' and self.mario.lives == 0:
            self.barrels = []
            self.barrel_number = 0
            pyxel.quit()
        for barrels in self.barrels:
            if (self.mario.x+14 >= barrels.positionx and self.mario.x <= barrels.positionx+11) and ((self.mario.y <= barrels.positiony+13 and self.mario.y-14 <= barrels.positiony and self.mario.y+16 >= barrels.positiony+14) or (self.mario.y+16 >= barrels.positiony+2 and self.mario.y+25 <= barrels.positiony+14 and self.mario.y <= barrels.positiony)):
                self.mario.lives -= 1
                self.state ='Dying'
                pyxel.play(1,1)
                pass
            elif (self.mario.x >= barrels.positionx + 5.75 and self.mario.x <=barrels.positionx + 10) and self.mario.y+15 < barrels.positiony+5 and self.mario.y+15 >= barrels.positiony-20 and not self.mario.climbing and self.mario.y > 8:
                self.mario.point += 100
                pyxel.play(0,0)
            else:
                self.state == 'Alive'

    def draw(self):
        '''Here we draw all the elements of the board, such as mario, the platforms, the ladders, the barrels, Donkey Kong 
        and Pauline, for the platforms we use a loop and differenciate between platforms by the position of the coordinates i
        nside the list, and draw the platform to the left or to the right. Then we use a loop to print the ladders (broken and non-broken) 
        and the barrels using lists, then the text shown in screen and finally we print mario, Pauline and Donkey Kong. We put all that 
        instide a condition which is if mario has won the game or not, so that when he wins the board changes and turns white with the message 
        "you have won" and the points'''
        pyxel.cls(0)
        if self.mario.win == False:
            pyxel.cls(0)
            #----------------Printing Platforms---------------------------------------
            for x in range (len(self.platforms.positiony)):
                positiony = self.platforms.positiony
                if x == 0:
                    positionx = 96
                    while positionx <224:
                        pyxel.blt(positionx,positiony[x],0,self.platforms.InitX,self.platforms.InitY,self.platforms.FinalX,self.platforms.FinalY,colkey = 0)
                        positionx += 32
                if x%2 != 0 and x != 0:
                    positionx = 0
                    while positionx < 224:
                        pyxel.blt(positionx,positiony[x],0,self.platforms.InitX,self.platforms.InitY,self.platforms.FinalX,self.platforms.FinalY,colkey = 0)
                        positionx += 32
                if x%2 == 0 and x != 0 and x != 6:
                    positionx = 32
                    while positionx < 256:
                        pyxel.blt(positionx,positiony[x],0,self.platforms.InitX,self.platforms.InitY,self.platforms.FinalX,self.platforms.FinalY,colkey = 0)
                        positionx += 32
                if x == 6:
                    positionx = 0
                    while positionx < 256:
                        pyxel.blt(positionx,positiony[x],0,self.platforms.InitX,self.platforms.InitY,self.platforms.FinalX,self.platforms.FinalY,colkey = 0)
                        positionx += 32
            #--------------------------------------------------------------------------
            
            #-------------------------Printing ladders---------------------------------
            for z in range (len(self.ladders.LaddersX)):#All Ladders
                b = self.ladders.LaddersX[z]
                c = self.ladders.LadderY[z]
                pyxel.blt(b,c,0,self.ladders.InitX,self.ladders.InitY,self.ladders.FinalX,self.ladders.FinalY,colkey = 0)
            #--------------------------------------------------------------------------
            
            #--------------------printing broken ladders-------------------------------
            for z in range(len(self.Bladders.bladdersX)):#All Broken Ladders
                b = self.Bladders.bladdersX[z]
                c = self.Bladders.bladdersY[z]
                pyxel.blt(b,c,0,self.Bladders.InitX,self.Bladders.InitY,self.Bladders.FinalX,self.Bladders.FinalY,colkey = 0)
            #--------------------------------------------------------------------------
            
            #-------------------------Printing barrels---------------------------------
            for barrel in self.barrels:#All Barrels
                pyxel.blt(barrel.positionx,barrel.positiony,0,barrel.InitX,barrel.InitY,barrel.FinalX,barrel.FinalY,colkey = 0)
            #--------------------------------------------------------------------------
                
            #----------------------Printing static barrels-----------------------------
            for z in range (len(self.Sbarrels.barrelsX)):#All Static Barrels
                b = self.Sbarrels.barrelsX[z]
                c = self.Sbarrels.barrelsY[z]
                pyxel.blt(b,c,0,self.Sbarrels.InitX,self.Sbarrels.InitY,self.Sbarrels.FinalX,self.Sbarrels.FinalY,colkey = 0)
            #--------------------------------------------------------------------------
            
            
            #--------------------------Printing text-----------------------------------
            pyxel.text(200, 10, "Lifes:", pyxel.frame_count % 16)#Lifes(word)
            pyxel.text(230, 10, str(self.mario.lives), pyxel.frame_count % 16)#Lifes(number)
            pyxel.text(200, 0, "Points:", pyxel.frame_count % 16)#Points(word)
            pyxel.text(230,0,str(self.mario.point),pyxel.frame_count % 16)#Points(number)
            #--------------------------------------------------------------------------
            
            #-----------------------Printing characters--------------------------------
            
            pyxel.blt(self.Donkey.positionx,self.Donkey.positiony,0,self.Donkey.InitX,self.Donkey.InitY,self.Donkey.FinalX,self.Donkey.FinalY,colkey = 0)#Donkey Kong
            pyxel.blt(self.pauline.positionx,self.pauline.positiony,0,self.pauline.InitX,self.pauline.InitY,self.pauline.FinalX,self.pauline.FinalY,colkey = 0)#Pauline    
            pyxel.blt(self.mario.x,self.mario.y, 0,self.mario.InitX,self.mario.InitY,self.mario.FinalX,self.mario.FinalY, colkey=0)#Mario
            #-------------------------------------------------------------------------
        else:
            pyxel.cls(7)
            pyxel.text(95, 120, "YOU HAVE WON", pyxel.frame_count % 16)
            pyxel.text(95, 130, "points:", 0)
            pyxel.text(125, 130, str(self.mario.point), 0)
        
            
Board()
        