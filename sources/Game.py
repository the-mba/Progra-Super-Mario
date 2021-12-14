from random import randint

import pyxel
from Mario import Mario
from Solid import Block, Goomba, Pipe
from GUI import GUI
from Helper import *
from Helper import BLOCK_TYPES as B_T
from My_Collection import My_Collection

class Game:
    def __init__(self) -> None:

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, caption="Pyxel Jump")
        pyxel.load("../assets/marioassets_133.pyxres")

        self.x = 0
        self.gui = GUI()
        self.mario = Mario(
            MARIO_STARTING_X, MARIO_STARTING_Y,
            MARIO_CONSTANT_VEL_X, MARIO_STARTING_VEL_Y,
            FLOOR_HEIGHT,
            BACKGROUND_RIGHT_MOVEMENT_THRESHOLD,
            GRAVITY,
            JUMPING_COEFFICIENT,
            PERSISTENT=True
        )


        self.solids = My_Collection(Goomba, Block, Pipe)


        self.goombas, self.blocks, self.pipes = self.solids.list
        
        self.goombas.new(B_T.goomba, 42 * 8, MARIO_STARTING_Y + OFFSET, 0, 0, FLOOR_HEIGHT)

        self.blocks.new(B_T.brick, 39 * 8, 80 + OFFSET,  0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.question, 41 * 8, 80 + OFFSET, 0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.brick, 43 * 8, 80 + OFFSET,  0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.question, 45 * 8, 80 + OFFSET, 0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.brick, 47 * 8, 80 + OFFSET,  0, 0, FLOOR_HEIGHT) # EL TILEMAP de altura 84 SE QUEDA EN EL PIXEL de altura 80 !!!

        self.pipes.new(B_T.pipe, 56*8 + OFFSET, 80 + 3 * 16, 0, 0, FLOOR_HEIGHT, 2)
        self.pipes.new(B_T.pipe, 72*8 + OFFSET, 80 + 1 * 16, 0, 0, FLOOR_HEIGHT, 4)

        self.goombas.new(B_T.goomba, 76 * 8, MARIO_STARTING_Y + OFFSET, 0, 0, FLOOR_HEIGHT)

        self.pipes.new(B_T.pipe, 96*8 + OFFSET, 80 - 8, 0, 0, FLOOR_HEIGHT, 5.5)

        self.goombas.new(B_T.goomba, 106 * 8, MARIO_STARTING_Y + OFFSET, 0, 0, FLOOR_HEIGHT)
        self.goombas.new(B_T.goomba, 110 * 8, MARIO_STARTING_Y + OFFSET, 0, 0, FLOOR_HEIGHT)

        self.pipes.new(B_T.pipe, 120*8 + OFFSET, 80 - 8, 0, 0, FLOOR_HEIGHT, 5.5)

        self.blocks.new(B_T.brick, 146 * 8, 80 + 1*16 + OFFSET,  0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.question, 148 * 8, 80 + 1*16 + OFFSET, 0, 0, FLOOR_HEIGHT)
        self.blocks.new(B_T.brick, 150 * 8, 80 + 1*16 + OFFSET,  0, 0, FLOOR_HEIGHT)


        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # advance background and move back Mario
        if self.mario.update(self.x * 8):
            self.x += BACKGROUND_SPEED
        
        self.solids.update(self)

    def draw(self) -> None:

        self.gui.draw(self.x, self.mario.points, self.mario.coins, self.mario.time)

        self.mario.draw(self.x * 8)

        self.solids.draw(self.x * 8)

        

        

Game()