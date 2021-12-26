import pyxel
from Helper import *

class GUI:
    def __init__(self) -> None:
        self.background = GUI.Background()
    
    def update(self) -> None:
        self.background.update()
        
    def draw(self, game) -> None:
        self.background.draw(game)

        #draw coin
        pyxel.blt(GAME_WIDTH * POS_COINS - 8 - 2, 4, 0, 48, 104, 8, 8, 7) # -8 is the coind GAME_WIDTH, -2 is some spacing

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
    
    class Background:
        def update(self) -> None:
            pass

        def draw(self, game) -> None:
            # draw light blue background
            pyxel.cls(12)

            # draw tilemap
            pyxel.bltm(0 + game.x % 8, 0, 0, game.x // 8, 74, 128, 128)

            # pyxel.bltm(0, 0, 0, game.x % 256 - 256, 74, 128, 128) # TODO: remove this and convert all coordinates to modulo 256 so that the whole game can infinitely repeat to the right
