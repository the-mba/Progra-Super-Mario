from random import randint

import pyxel
from Mario import Mario
from Entity import *
import Helper
from Helper import BLOCK_TYPES as B_T
from My_Collection import My_Collection

class Game:
    def __init__(self) -> None:

        # INIT
        game = self

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, caption="New Super Mario Bros.")
        pyxel.load("../assets/marioassets.pyxres")

        game.x = 0
        game.mario = Mario(game)

        # COLLECTIONS
        game.bricks = My_Collection(STARTING_BRICKS)
        game.question_bricks = My_Collection(STARTING_QUESTION_BRICKS)
        game.clear_bricks = My_Collection(STARTING_CLEAR_BRICKS)
        game.goombas = My_Collection(STARTING_GOOMBAS)
        game.pipes = My_Collection(STARTING_PIPES)
        game.decors = My_Collection(STARTING_DECORS)

        game.blocks = My_Collection(game.bricks, game.question_bricks, game.clear_bricks)
        game.solid = My_Collection(game.blocks, game.goombas, game.pipes, game.decors)

        # ENTITIES
        game.bricks.add(Brick(              game,    39 * 8,    80 + OFFSET))
        game.bricks.add(Question_Brick(     game,    41 * 8,    80 + OFFSET))
        game.bricks.add(Brick(              game,    43 * 8,    80 + OFFSET))
        game.bricks.add(Question_Brick(     game,    45 * 8,    80 + OFFSET))
        game.bricks.add(Brick(              game,    47 * 8,    80 + OFFSET)) # EL TILEMAP a la altura 84 se queda en la pantalla en el pixel de altura 80 !!!

        game.bricks.add(Brick(              game,   146 * 8,    96 + OFFSET))
        game.bricks.add(Question_Brick(     game,   148 * 8,    96 + OFFSET))
        game.bricks.add(Brick(              game,   150 * 8,    96 + OFFSET))

        game.clear_bricks.add(Clear_Brick(  game,   140 * 8,   144 + OFFSET))

        game.decors.add(Decor(              game,        30,             88))

        # game.blocks.new(B_T.mushroom, 110, 144))

        pyxel.run(game.update, game.draw)

    def update(self) -> None:
        game = self

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # update mario returns the extra x to move_right
        game.x += game.mario.update()
        
        game.solids.update()

    def draw(self) -> None:
        game = self

        game.draw_background_and_gui()

        game.solids.draw()

        game.mario.draw()
    
    def draw_background_and_gui(self):
        game = self

        # draw light blue background
        pyxel.cls(12)
        # draw tilemap
        pyxel.bltm(- (game.x % 8), 0, 0, game.x // 8, 74, 128, 128)
        # pyxel.bltm(0, 0, 0, game.x % 256 - 256, 74, 128, 128) # TODO: remove this and convert all coordinates to modulo 256 so that the whole game can infinitely repeat to the right

        #draw coin
        pyxel.blt(GAME_WIDTH * POS_COINS - 8 - 2, 4, 0, 48, 104, 8, 8, 7) # -8 is the coind GAME_WIDTH, -2 is some spacing
        pyxel.text(GAME_WIDTH * 0.6, 80, str(game.mario.x), 1)

        # draw texts
        name_str = "MARIO"
        pyxel.text(GAME_WIDTH * POS_POINTS, 4, name_str, 1)
        pyxel.text(GAME_WIDTH * POS_POINTS + 1, 4, name_str, 7)
        if DEBUG: game.points = 0
        points_str = f'{game.points:06d}'
        pyxel.text(GAME_WIDTH * POS_POINTS, 10, points_str, 1)
        pyxel.text(GAME_WIDTH * POS_POINTS + 1, 10, points_str, 7)
        if DEBUG: mario_coins = 0
        coins_str = 'x' + f'{mario_coins:02d}'
        pyxel.text(GAME_WIDTH * POS_COINS, 6, coins_str, 1)
        pyxel.text(GAME_WIDTH * POS_COINS + 1, 6, coins_str, 7)
        world_str = "WORLD"
        pyxel.text(GAME_WIDTH * POS_WORLD + 1, 4, world_str, 1)
        pyxel.text(GAME_WIDTH * POS_WORLD, 4, world_str, 7)
        world_name = "1 - 1"
        pyxel.text(GAME_WIDTH * POS_WORLD, 10, world_name, 1)
        pyxel.text(GAME_WIDTH * POS_WORLD + 1, 10, world_name, 7)
        time_name = "TIME"
        pyxel.text(GAME_WIDTH * POS_TIME, 4, time_name, 1)
        pyxel.text(GAME_WIDTH * POS_TIME + 1, 4, time_name, 7)
        if DEBUG: mario_time = 0
        time_name = f'{mario_time:02d}'
        pyxel.text(GAME_WIDTH * POS_TIME, 10, time_name, 1)
        pyxel.text(GAME_WIDTH * POS_TIME + 1, 10, time_name, 7)