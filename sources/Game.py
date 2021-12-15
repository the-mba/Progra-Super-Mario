from random import randint

import pyxel
from Mario import Mario
from Entity import *
from GUI import GUI
from Helper import *
from Helper import BLOCK_TYPES as B_T
from My_Collection import My_Collection

class Game:
    def __init__(self) -> None:

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, caption="Pyxel Jump")
        pyxel.load("../assets/marioassets.pyxres")

        self.x = 0
        self.gui = GUI()
        self.mario = Mario()
        self.solids = My_Collection(Goomba, Block, Pipe, Decor)

        self.goombas, self.blocks, self.pipes, self.decors = self.solids.list
        
        self.goombas.new(B_T.goomba, 42 * 8, 144 + OFFSET, 3, 0)

        self.blocks.new(B_T.brick, 39 * 8, 80 + OFFSET,  0, 0)
        self.blocks.new(B_T.brick_question, 41 * 8, 80 + OFFSET, 0, 0)
        self.blocks.new(B_T.brick, 43 * 8, 80 + OFFSET,  0, 0)
        self.blocks.new(B_T.brick_question, 45 * 8, 80 + OFFSET, 0, 0)
        self.blocks.new(B_T.brick, 47 * 8, 80 + OFFSET,  0, 0) # EL TILEMAP de altura 84 SE QUEDA EN EL PIXEL de altura 80 !!!

        self.pipes.new(B_T.pipe, 56*8 + OFFSET, 80 + 3 * 16, 0, 0, 2)
        self.pipes.new(B_T.pipe, 72*8 + OFFSET, 80 + 1 * 16, 0, 0, 4)

        self.goombas.new(B_T.goomba, 76 * 8, 144 + OFFSET, 3, 0)

        self.pipes.new(B_T.pipe, 96*8 + OFFSET, 80 - 8, 0, 0, 5.5)

        self.goombas.new(B_T.goomba, 106 * 8, 144 + OFFSET, 0, 0)
        self.goombas.new(B_T.goomba, 110 * 8, 144 + OFFSET, 0, 0)

        self.pipes.new(B_T.pipe, 120*8 + OFFSET, 80 - 8, 0, 0, 5.5)

        self.blocks.new(B_T.brick, 146 * 8, 80 + 1*16 + OFFSET,  0, 0)
        self.blocks.new(B_T.brick_question, 148 * 8, 80 + 1*16 + OFFSET, 0, 0)
        self.blocks.new(B_T.brick, 150 * 8, 80 + 1*16 + OFFSET,  0, 0)

        self.blocks.new(B_T.brick_clear, 140 * 8, 144 + OFFSET, 0, 0)

        self.decors.new(B_T.cloud, 30, 88, 0, 0)

        # self.blocks.new(B_T.mushroom, 110, 144, 0, 0)

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # advance background and move back Mario
        if self.mario.update(self.x * 8):
            self.x += BACKGROUND_SPEED
        
        self.solids.update(self)

    def draw(self) -> None:

        self.gui.draw(self)

        self.solids.draw(self)

        self.mario.draw(self)

        

        

Game()