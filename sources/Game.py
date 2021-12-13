from random import randint

import pyxel
from Mario import Mario
from GUI import GUI

DEBUG = 1

MARIO_STARTING_X = 40
MARIO_STARTING_Y = 82
MARIO_STARTING_VEL_Y = 0
MARIO_CONSTANT_VEL_X = 2
GRAVITY = 0.5
JUMPING_COEFFICIENT = 0.5

MARIO_TALLNESS = 16
MARIO_WIDTH = MARIO_TALLNESS
MARIO_SPRITE_X = 0
MARIO_SPRITE_Y = 48

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
            MARIO_STARTING_X, MARIO_STARTING_Y,
            MARIO_CONSTANT_VEL_X, MARIO_STARTING_VEL_Y,
            MARIO_WIDTH, MARIO_TALLNESS,
            MARIO_SPRITE_X, MARIO_SPRITE_Y,

            FLOOR_HEIGHT,
            BACKGROUND_RIGHT_MOVEMENT_THRESHOLD,
            GRAVITY,
            JUMPING_COEFFICIENT
        )

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # advance background and move back Mario
        if self.mario.update(self):
            self.gui.update()
            self.x += BACKGROUND_SPEED

    def draw(self) -> None:    

        self.gui.draw(self.mario.points, self.mario.coins, self.mario.time)    

        self.mario.draw()

        

        

Game()