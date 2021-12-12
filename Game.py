from random import randint

import pyxel
from Mario import Mario

DEBUG = 1

PLAYER_STARTING_X = 40
PLAYER_STARTING_Y = 82
PLAYER_STARTING_VEL_Y = 0
PLAYER_VEL_X = 2
GRAVITY = 0.4

PLAYER_TALLNESS = 16
SCALE = 2
WIDTH = 256
HEIGHT = 256
BACKGROUND_RIGHT_MOVEMENT_THRESHOLD = 70
FLOOR_HEIGHT = HEIGHT - 22

class Game:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="Pyxel Jump")

        pyxel.load("assets/marioassets_133.pyxres")

        self.background = pyxel.tilemap(0)

        self.mario = Mario(PLAYER_STARTING_X, PLAYER_STARTING_Y)

        self.background_position = 0

        self.score = 0
        self.player_x = PLAYER_STARTING_X
        self.player_y = PLAYER_STARTING_Y
        self.player_vel_y = PLAYER_STARTING_VEL_Y
        self.player_alive = True

        pyxel.run(self.update, self.draw)

    def height(self):
        return FLOOR_HEIGHT - PLAYER_TALLNESS - self.player_y

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.mario.update(self)

        # advance background
        if self.player_x > WIDTH - BACKGROUND_RIGHT_MOVEMENT_THRESHOLD:
            self.background_position += 1/4 #(self.player_x - (WIDTH - BACKGROUND_RIGHT_MOVEMENT_THRESHOLD)) * 1/8
            self.player_x = WIDTH - BACKGROUND_RIGHT_MOVEMENT_THRESHOLD

    def draw(self):
        pyxel.cls(12)

        # draw sky
        pyxel.bltm(0, 50, 0, self.background_position, 88, 160, 32)
        

        # draw player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            0 if self.player_vel_y > 0 else 0,
            48,
            16,
            16,
            12
        )

        #draw coin of GUI
        pyxel.blt(40, 4, 0, 48, 104, 8, 8, 7)

        # draw texts
        name_str = "MARIO"
        pyxel.text(5, 4, name_str, 1)
        pyxel.text(4, 4, name_str, 7)
        if DEBUG: self.mario.coins = 0
        points_str = f'{self.mario.coins:06d}'
        pyxel.text(5, 10, points_str, 1)
        pyxel.text(4, 10, points_str, 7)
        if DEBUG: self.mario.coins = 0
        coins_str = 'x' + f'{self.mario.coins:02d}'
        pyxel.text(50, 6, coins_str, 1)
        pyxel.text(51, 6, coins_str, 7)
        world_str = "WORLD"
        pyxel.text(70, 4, world_str, 1)
        pyxel.text(71, 4, world_str, 7)
        world_name = "1 - 1"
        pyxel.text(70, 10, world_name, 1)
        pyxel.text(71, 10, world_name, 7)
        time_name = "TIME"
        pyxel.text(110, 4, time_name, 1)
        pyxel.text(111, 4, time_name, 7)
        if DEBUG: self.mario.time = 0
        time_name = f'{self.mario.time:02d}'
        pyxel.text(110, 10, time_name, 1)
        pyxel.text(111, 10, time_name, 7)

Game()