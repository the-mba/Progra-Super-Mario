from random import randint

import pyxel
from Mario import Mario
from Solid import Block, Goomba, Pipe
from GUI import GUI
from Helper import BLOCK_TYPES as B_T
from My_Collection import My_Collection
from My_Collection import My_Meta_Collection

DEBUG = 1

GAME_WIDTH = 256
GAME_HEIGHT = 192
BACKGROUND_RIGHT_MOVEMENT_THRESHOLD = GAME_WIDTH * 0.6
BACKGROUND_SPEED = 1
FLOOR_HEIGHT = GAME_HEIGHT - 32

OFFSET = -4

MARIO_TALLNESS = 16
MARIO_WIDTH = MARIO_TALLNESS
MARIO_SPRITE_X = 0
MARIO_SPRITE_Y = 48

MARIO_STARTING_X = 160
MARIO_STARTING_Y = FLOOR_HEIGHT - MARIO_TALLNESS
MARIO_STARTING_VEL_Y = 0
MARIO_CONSTANT_VEL_X = 2
GRAVITY = 0.5
JUMPING_COEFFICIENT = 1.8


class Game:
    def __init__(self) -> None:

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, caption="Pyxel Jump")
        pyxel.load("../assets/marioassets_133.pyxres")

        self.x = 0
        self.gui = GUI(DEBUG, GAME_WIDTH, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD, BACKGROUND_SPEED)
        self.mario = Mario(
            MARIO_STARTING_X, MARIO_STARTING_Y,
            MARIO_CONSTANT_VEL_X, MARIO_STARTING_VEL_Y,
            FLOOR_HEIGHT,
            BACKGROUND_RIGHT_MOVEMENT_THRESHOLD,
            GRAVITY,
            JUMPING_COEFFICIENT,
            PERSISTENT=True
        )

        self.solids = My_Meta_Collection(Goomba, Block, Pipe)

        self.goombas, self.blocks, self.pipes = self.solids.list
        
        self.goombas.new(B_T.goomba, 42 * 8, MARIO_STARTING_Y + OFFSET, 0, 0, FLOOR_HEIGHT)

        self.blocks.new(B_T.brick, 39 * 8, 80 + OFFSET,  0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.question, 41 * 8, 80 + OFFSET, 0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.brick, 43 * 8, 80 + OFFSET,  0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.question, 45 * 8, 80 + OFFSET, 0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.brick, 47 * 8, 80 + OFFSET,  0, 0, FLOOR_HEIGHT)

        self.pipes.new(B_T.pipe, 80, 80, 0, 0, 20, FLOOR_HEIGHT, True)
        print("length of pipe is supposed to be: ", len(self.pipes.list))
        for i in self.pipes.list[0].parts.list:
            print(i)

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # advance background and move back Mario
        if self.mario.update(self.x * 8):
            self.x += BACKGROUND_SPEED
        
        self.goombas.update(self.mario)

    def draw(self) -> None:

        self.gui.draw(self.x, self.mario.points, self.mario.coins, self.mario.time)    

        self.mario.draw(self.x * 8)

        self.solids.draw(self.x * 8)

        

        

Game()