from random import randint

import pyxel
from Mario import Mario
from GUI import GUI

DEBUG = 1

PLAYER_STARTING_X = 40
PLAYER_STARTING_Y = 82
PLAYER_STARTING_VEL_Y = 0
PLAYER_CONSTANT_VEL_X = 2
GRAVITY = 0.5
JUMPING_COEFFICIENT = 0.2

PLAYER_TALLNESS = 16
SCALE = 2
WIDTH = 256
HEIGHT = 192
BACKGROUND_RIGHT_MOVEMENT_THRESHOLD = WIDTH - 70
BACKGROUND_SPEED = 1/2
FLOOR_HEIGHT = HEIGHT - 32

class Game:
    def __init__(self) -> None:

        pyxel.init(WIDTH, HEIGHT, caption="Pyxel Jump")
        pyxel.load("../assets/marioassets_133.pyxres")

        self.x = 0
        self.gui = GUI(DEBUG, WIDTH, self.x, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD, BACKGROUND_SPEED)
        self.mario = Mario(
            PLAYER_STARTING_X,
            PLAYER_STARTING_Y,
            PLAYER_CONSTANT_VEL_X,
            PLAYER_STARTING_VEL_Y,
            FLOOR_HEIGHT,
            PLAYER_TALLNESS,
            GRAVITY,
            JUMPING_COEFFICIENT
        )

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.mario.update(self)

        # advance background and move back Mario
        self.mario.x = self.gui.update(self.mario.x)

    def draw(self) -> None:    

        self.gui.draw(self.mario.points, self.mario.coins, self.mario.time)    

        self.mario.draw()

        

        

Game()